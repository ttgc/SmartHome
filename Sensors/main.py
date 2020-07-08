#!usr/bin/env python3
#-*-coding:utf-8-*-

import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from httpRequester import postTemperature, getSettings, postSettings
from TemperatureSimulator import *

def run():
    print("hello world!")
    tS = TemperatureSimulator()
    while(True):
        time.sleep(1)
        t = tS.getTemperature()
        print("Send Temperature : " + str(t))
        r = postTemperature(t)
        h = r.json().get("heat_on")
        c = r.json().get("clim_on")
        tS.setHeatClim(h,c)
        print(r.text)
    #print("Settings :")
    #print(getSettings().text)
    print("Bye Bye !")

run()
