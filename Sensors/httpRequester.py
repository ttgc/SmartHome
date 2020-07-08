#!usr/bin/env python3
#-*-coding:utf-8-*-

import requests

EdgePath = "https://localhost:5001/"
SettingsPath = "api/Settings"
TemperaturePath = "api/Temperature"

#basic class to encapsulate the http commands
class httpRequester:
    def __init__(self, path):
        self._path = path

    def get():
        return requests.get(self._path)

    def post(v):
        return requests.post(self._path, data = v)

temperatureRequester = httpRequester(EdgePath + TemperaturePath)
settingsRequester = httpRequester(EdgePath + SettingsPath)
