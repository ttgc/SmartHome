#!usr/bin/env python3
#-*-coding:utf-8-*-

import os, ssl

from httpRequester import postTemperature, getSettings, postSettings

def run():
    print("hello world!")
    print("Temperature :")
    print(postTemperature(23).text)
    print("Settings :")
    print(getSettings().text)
    print("Bye Bye !")

run()
