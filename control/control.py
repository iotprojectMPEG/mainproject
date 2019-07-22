#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script...
"""
import json
import sys, os
import threading
import requests
import time
import datetime
from rain_control import rain_control

FILE1 = "conf.json"
LIST = []

#
# def write_catalog(filename):


def read_file(filename):
    """Read json file to get catalogURL, port and gardenID."""
    with open(filename, "r") as f:
        data = json.loads(f.read())
        url = data["catalogURL"]
        port = data["port"]
        gardenID = data["gardenID"]
        return (url, port, gardenID)


class Plant(threading.Thread):
    def __init__(self, ThreadID, name, plantID, hours):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name
        self.plantID = plantID
        self.hours = hours

    def run(self):

        sec = rain_control.get_result()
        h = datetime.datetime.strptime(self.hours, '%H:%M')
        h = h + datetime.timedelta(seconds=sec)
        h = format(h, '%H:%M')
        print(h)

        ######################################################################
        # TO DO: write modification on dynamic part of the catalog.
        ######################################################################

class UpdateList(threading.Thread):
    """Updates global list of plants every day. If the list is the same as
    before, it does not update it.
    """
    def __init__(self, ThreadID, name):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.name = name

    def run(self):
        global LIST
        while True:
            new_list = []
            url, port, gardenID = read_file(FILE1)
            string = "http://" + url + ":" + port + "/static"
            data = json.loads(requests.get(string).text)
            for g in data["gardens"]:
                if g["gardenID"] == gardenID:
                    for p in g["plants"]:
                        new_list.append(p["plantID"])

            if LIST != new_list:
                LIST = new_list
                print("New list: ", LIST)
            else:
                print("List is up to date.")

            time.sleep(86400)

def main():
    upd = UpdateList(1, "UpdateList")
    upd.start()

    plt = Plant(2, "Plant", "p_1001", "08:00")
    plt.start()

if __name__ == '__main__':
    main()