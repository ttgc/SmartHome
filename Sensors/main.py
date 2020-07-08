#!usr/bin/env python3
#-*-coding:utf-8-*-

import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #in order to avoid warning for each http request

from httpRequester import postTemperature
from TemperatureSimulator import *

#this program is run by the sensors giving temperature, it does not asks for settings
def run():
    print("hello world!")
    tS = TemperatureSimulator()
    while(True):
        time.sleep(1)
        t = tS.getTemperature()
        print("Send Temperature : " + str(t) + " °C")
        r = postTemperature(t)
        h = r.json().get("heat_on")
        c = r.json().get("clim_on")
        tS.setHeatClim(h,c)
        print(r.text)
    print("Bye Bye !")

run()
