#!usr/bin/env python3
#-*-coding:utf-8-*-

import time

from httpRequester import postTemperature, getSettings, postSettings
from TemperatureSimulator import *

def run():
    print("hello world!")
    tS = TemperatureSimulator()
    while(True):
        time.sleep(1)
        t = tS.getTemperature()
        print("Send Temperature : " + str(t))
        print(postTemperature(t).text)
    #print("Settings :")
    #print(getSettings().text)
    print("Bye Bye !")

run()
