#!usr/bin/env python3
#-*-coding:utf-8-*-

import time

def timer(fct):
    def timingFunction(*args, **kargs):
        start = time.time()
        result = fct(*args, **kargs)
        end = time.time()
        totalTime = end - start
        print(f"Temps d'exécution de la fonction {fct} : {totalTime} s")
        return result
    return timingFunction
