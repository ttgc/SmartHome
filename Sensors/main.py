#!usr/bin/env python3
#-*-coding:utf-8-*-

import argparse

parser = argparse.ArgumentParser(description='Simulate a sensor, sending temperature in C to the edge server')
parser.add_argument("-n", "--number-post", dest='NbPost', default=1, help="Number of post in each unit of time", type=int)
parser.add_argument("-t", "--time-period", dest='delta_time', default=1, help="Period between each calculation and post, in seconds", type=int)
parser.add_argument("-p", "--plot", dest='isPlotting', action='store_const',
                    const=True, default=False, help="Display the ploting of data at the end of program")

import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #in order to avoid warning for each http request

from httpRequester import postTemperature
from TemperatureSimulator import *

from timer import plotData
import atexit

#this program is run by the sensors giving temperature, it does not asks for settings
def run():
    print("hello world!")
    args = parser.parse_args()
    if args.isPlotting:
        atexit.register(plotData)
    tS = TemperatureSimulator()
    #in seconds
    print("Temperature will be calculated every " + str(args.delta_time) + "s")
    while(True):
        time.sleep(args.delta_time)
        for i in range(args.NbPost):
            t = tS.getTemperature()
            print("Send Temperature : " + str(t) + " °C")
            r = postTemperature(t)
            h = r.json().get("heat_on")
            c = r.json().get("clim_on")
            tS.setHeatClim(h,c)
            print(r.text)
    print("Bye Bye !")

run()
