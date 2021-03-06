# IoT for Smart Gardening
![Python Version](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-informational?style=flat&logo=python&logoColor=white) 
![GitHub](https://img.shields.io/github/contributors/iotprojectMPEG/mainproject?style=flat&logo=github)
![GitHub](https://img.shields.io/github/license/iotprojectMPEG/mainproject?style=flat)
![Poetry](https://img.shields.io/badge/Poetry-2f2f55?style=flat&link=https://python-poetry.org)

Internet of Things project for smart gardening.
## Info
### University
Politecnico di Torino / Polytechnic University of Turin

![](http://www.politocomunica.polito.it/var/politocomunica/storage/images/media/images/marchio_logotipo_politecnico/1371-1-ita-IT/marchio_logotipo_politecnico_medium.jpg)
### Course
Master of Science program in **ICT for Smart Societies**

01QWRBH - **Programming for IoT applications**

<img src="https://didattica.polito.it/zxd/cms_data/image/6/ICT4SS_AzarSHABANI_Matr204782.jpg" width="200" />

## Documentation
Complete documentation of code can be found in docstrings of the scripts and on [SmartGarden Wiki](https://github.com/iotprojectMPEG/mainproject/wiki).

## Getting started
### Tools
- Python 3.6 or higher
- MQTT message broker
### Installation of packages
It is recommended to setup a virtual environment in order to use specific versions of Python packages. The following instructions will help you in setting up the virtual environment with the help of [Poetry](https://python-poetry.org/). If you want to use a different software you can find the required packages in [pyproject.toml](https://github.com/iotprojectMPEG/mainproject/blob/master/pyproject.toml) under ```[tool.poetry.dependencies]```.
#### Virtual environment with Poetry
* Install [Poetry](https://github.com/python-poetry/poetry#Installation):
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
* Recommended: Configure Poetry it in order to create a virtual environment in a ```.venv``` folder inside the project directory:
```sh
poetry config virtualenvs.in-project true
```
* cd in project directory.
* Create the virtual environment and install Python packages and dependencies:
``` sh
poetry install
```
* Activate the virtual environment:

Linux:
``` sh
source .venv/bin/activate
```
Windows:
``` sh
.venv\Scripts\activate
```
### Config files
* Rename [api.json.example](https://github.com/iotprojectMPEG/mainproject/blob/master/catalog/api.json.example) in **api.json**. Then you can fill this file with all secret information like channel IDs of ThingSpeak.
* You can set all IP addresses, ports and Telegram token by running [set-ip.py](https://github.com/iotprojectMPEG/mainproject/blob/master/set-ip.py) and following the instructions on screen:
``` sh
./set-ip-py
```
* Go to [Sensors installation](https://github.com/iotprojectMPEG/mainproject/blob/master/README.md#sensors-installation) in order to setup your sensors.
### Run the system
#### Catalog
``` sh
./catalog/catalog.py
```

#### ThingSpeak adaptor
``` sh
./thingspeak/thingspeak.py
```

#### Sensors
* Run all scripts of your [sensors](https://github.com/iotprojectMPEG/mainproject/tree/master/sensors).

#### Strategies
* Run [all your strategies](https://github.com/iotprojectMPEG/mainproject/tree/master/control).

#### Telegram bot
``` sh
./telegram-bot/bot.py
```

#### Freeboard
``` sh
./freeboard/freeboard.py
```

#### QT Interface
This allows you to add gardens, plants and devices.
``` sh
./interface/interface.py
```

## Sensors installation
### Temperature and humidity sensor (DHT11)
<img src="https://github.com/iotprojectMPEG/mainproject/blob/master/sensors/images/dht11.png" width="500" />

### Rain sensor
<img src="https://github.com/iotprojectMPEG/mainproject/blob/master/sensors/images/rain.jpg" width="500" />

### Light sensor
<img src="https://github.com/iotprojectMPEG/mainproject/blob/master/sensors/images/light.jpg" width="400" /> 


## Team
- Fassio Edoardo  
- Grasso Paolo  
- Maffei Marzia  
- Rende Gennaro  

## License
[GPL-3.0](./LICENSE)
