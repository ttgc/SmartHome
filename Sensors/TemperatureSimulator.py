
import time
import math
import random

NOISE_INTENSITY = 0.3
HEAT_PER_SECOND = 0.0005
MIN_HEAT_T = -20
MAX_HEAT_T = 20
    
mMIN_T = 0
MMIN_T = 20
mMAX_T = 15
MMAX_T = 46
MIN_HOUR = 2
MAX_HOUR = 14

TOTAL_DAY_TIME_S = 3600 * 24.0

#the temperature simulator workd in degree, all time calculations are made inside of the class
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

    def applyHeatNClim(self):
        multiplier = 0
        if self.heat:
            multiplier += 1
        if self.clim:
            multiplier -= 1
        t = time.time()
        delta_t = t - self.prevTime
        self.deltaT += multiplier * delta_t * HEAT_PER_SECOND
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
        theta = (rt - MAX_HOUR * 3600) / TOTAL_DAY_TIME_S
        print(theta)
        delta = self.maxT - self.minT
        T += self.minT + delta * math.cos(theta)
        return T
    
