#!usr/bin/env python3
#-*-coding:utf-8-*-

import time
import math
import random

NOISE_INTENSITY = 0.15
HEAT_PER_SECOND = 0.0005
MIN_HEAT_T = -20
MAX_HEAT_T = 20
    
mMIN_T = -5 #minimum natural temperature at night
MMIN_T = 20 #maximum natural temperature at night
mMAX_T = 15 #minimum natural temperature at day
MMAX_T = 38 #maximum natural temperature at day

MAX_HOUR = 14 #Zenith

#time in one day in seconds
TOTAL_DAY_TIME_S = 3600 * 24.0

#the temperature simulator works in degree Celsius, all time calculations are made inside of the class
class TemperatureSimulator:
    
    def __init__(self, minT = None, maxT = None, heat = False, clim = False):
        if minT is None :
            self.minT = random.uniform(mMIN_T, MMIN_T)
        else:
            self.minT = minT
        if maxT is None :
            self.maxT = random.uniform(max(self.minT + 5, mMAX_T), MMAX_T)
        else:
            self.maxT = maxT
        self.heat = False
        self.clim = False
        self.deltaT = 0 #the added Temperature created by the heat/clim
        self.prevTime = time.time() #the last time heat was checked 

    def setHeat(self, h):
        self.applyHeatNClim()
        self.heat = h

    def setClim(self, c):
        self.applyHeatNClim()
        self.clim = c

    def setHeatClim(self, h, c):
        self.applyHeatNClim()
        self.heat = h
        self.clim = c

    def applyHeatNClim(self):
        multiplier = 0
        if self.heat:
            multiplier += 1
        if self.clim:
            multiplier -= 1
        t = time.time()
        delta_t = t - self.prevTime
        self.deltaT += multiplier * delta_t * HEAT_PER_SECOND
        self.deltaT = min(max(MIN_HEAT_T, self.deltaT), MAX_HEAT_T)
        self.prevTime = t
    
    def getTemperature(self):
        #noise
        T = random.uniform(-NOISE_INTENSITY, NOISE_INTENSITY)
        #heat
        self.applyHeatNClim()
        T += self.deltaT

        #"natural" temperature
        t = time.localtime()
        rt = t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec
        theta = 2 * math.pi * (rt - MAX_HOUR * 3600) / TOTAL_DAY_TIME_S
        delta = self.maxT - self.minT
        T += self.minT + delta * math.cos(theta)
        return T
    
