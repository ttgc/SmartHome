#!usr/bin/env python3
#-*-coding:utf-8-*-

from timer import *
import requests

EdgePath = "https://localhost:5001/"
SettingsPath = EdgePath + "api/Settings/"
TemperaturePath = EdgePath + "api/Temperature/"

@timer
def postTemperature(value):
    return requests.post(TemperaturePath + str(value), verify=False)

@timer
def getSettings():
    return requests.get(SettingsPath, verify=False)

@timer
def postSettings(d):
    print(d)
    return requests.post(SettingsPath, json = d, verify=False)
