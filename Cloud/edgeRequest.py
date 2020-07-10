#!usr/bin/env python3
#-*-coding:utf-8-*-

from timer import *
import requests

EdgePath = "https://localhost:5001/"
TemperaturePath = EdgePath + "api/Temperature/"

@timer
def getTemperature():
    return requests.get(TemperaturePath, verify=False)