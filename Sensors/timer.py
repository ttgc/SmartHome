#!usr/bin/env python3
#-*-coding:utf-8-*-

import time
import matplotlib.pyplot as plt

delta_t_list = []
AVERAGE = 0
MIN_VALUE = 10000
MAX_VALUE = 0

def plotData():
    average = sum(delta_t_list) / len(delta_t_list)
    minimum = min(delta_t_list)
    maximum = max(delta_t_list)
    print("Minimum : " + str(minimum))
    print("Maximum : " + str(maximum))
    print("Average : " + str(average))
    plt.plot(delta_t_list)
    plt.ylabel("Temps de réponse (s)")
    plt.show()

def timer(fct):
    def timingFunction(*args, **kargs):
        start = time.time()
        result = fct(*args, **kargs)
        end = time.time()
        totalTime = end - start
        delta_t_list.append(totalTime)
        print(f"Temps d'exécution de la fonction {fct} : {totalTime} s")
        return result
    return timingFunction
