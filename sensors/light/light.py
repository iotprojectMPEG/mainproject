#!/usr/bin/env python3
# Sono necessari i seguenti componenti (edo_fax li ha):
# 1. Photoresistor module
# 2. Un Analog to Digital Converter PCF 8591 (e installare la libreria)

#Istruzioni montaggio figura "light.jpg"
###################
# Light Intensity #
###################
import PCF8591 as ADC
import RPi.GPIO as GPIO
import json
import requests
import threading
import paho.mqtt.client as PahoMQTT
import os, sys, inspect
import time

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import updater

TOPIC = 'smartgarden/+/+/light'
FILENAME = "conf.json"

DO = 17
GPIO.setmode(GPIO.BCM)

def setup():
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)

class MyPublisher(object):
    def __init__(self, clientID, topic, serverIP, port):
        self.clientID = clientID
        self.topic = topic
        self.messageBroker = serverIP
        self.port = port
        self._paho_mqtt = PahoMQTT.Client(clientID, False)
        self._paho_mqtt.on_connect = self.my_on_connect
        #self._paho_mqtt.on_message = self.my_on_message_received
        self.loop_flag = 1

    def start(self):
        self._paho_mqtt.connect(self.messageBroker, self.port)
        self._paho_mqtt.loop_start()
        #self._paho_mqtt.subscribe(self.topic, 2)

    def stop(self):
        #self._paho_mqtt.unsubscribe(self.topic)
        self._paho_mqtt.loop_stop()
        self._paho_mqtt.disconnect()

    def my_on_connect(self, client, userdata, flags, rc):
        print ("Connected to %s - Result code: %d" % (self.messageBroker, rc))
        self.loop_flag = 0

    def my_publish(self, message):
        print("Publishing on %s:" % self.topic)
        print(json.dumps(json.loads(message), indent=2))
        self._paho_mqtt.publish(self.topic, message, 2)


class PubData(threading.Thread):
    def __init__(self, ThreadID, name):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name
        (self.devID, self.url, self.port) = updater.read_file("conf.json")
        print(">>> Light %s <<<\n" %(self.devID))
        (self.gardenID, self.plantID,
         self.resources) = updater.find_me(self.devID,
                                           self.url, self.port)
        (self.broker_ip, mqtt_port) = updater.broker_info(self.url, self.port)
        self.mqtt_port = int(mqtt_port)

        self.topic = []
        for r in self.resources:
            self.topic.append('smartgarden/' + self.gardenID + '/'
                              + self.plantID + '/' + r)

    def run(self):
        print("Topics:", self.topic)
        pub = MyPublisher(self.devID + '_1', self.topic[0], self.broker_ip,
                                     int(self.mqtt_port))
        pub.start()

        while pub.loop_flag:
            print("Waiting for connection...")
            time.sleep(1)

        while True:
            data = get_data(self.devID, self.resources)
            pub.my_publish(json.dumps(data))
            time.sleep(60)

        pub.stop()


def get_data(devID, res):
    value=None
    try:
        value = ADC.read(0)
    except:
        pass

    timestamp=time.time()
    data={
        "bn": devID,
        "e":[{
            "n":res[0]["n"],
            "u": res[0]["u"],
            "t": timestamp,
            "v": value
        }]
    }

    return data

if __name__ == '__main__':
    setup()

    thread1=updater.Alive(1,"Alive")
    thread2 = PubData(2, "PubData")

    thread1.start()
    time.sleep(1)
    thread2.start()



