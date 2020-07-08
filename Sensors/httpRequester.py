#!usr/bin/env python3
#-*-coding:utf-8-*-

import requests

EdgePath = "https://localhost:5001/"
SettingsPath = EdgePath + "api/Settings/"
TemperaturePath = EdgePath + "api/Temperature/"

def postTemperature(value):
    return requests.post(TemperaturePath + str(value), verify=False)

def getSettings():
    return requests.get(SettingsPath, verify=False)

def postSettings(data):
    return requests.post(SettingsPath, data = v, verify=False)
