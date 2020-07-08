#!usr/bin/env python3
#-*-coding:utf-8-*-

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #in order to avoid warning for each http request
from httpRequester import getSettings, postSettings

from settings import Settings

def help():
    print("Commands :")
    print("-'get' to get the current edge settings")
    print("-'help' or 'h' for the list of commands")
    print("-'load' to save in local the current edge settings")
    print("-'new' to create a new settings with default value")
    print("-'new <name> <clim_on> <clim_off> <heat_on> <heat_on> <temperature_unit>' to create a new settings in local")
    print("-'post' to post your local edge settings if it exists")
    print("-'quit' or 'q' to quit application")
    print("-'see' to see the current settings in local")
    print("-'set <element> <value>' to set in local one of the values, type 'set -h' for details")

def helpSet():
    print("'set <element> <value>' :")
    print("-<element> is either 'name', 'clim_off', 'clim_on', 'heat_off', 'heat_on' or 'unit'")
    print("-if <element> is clim_off/on or heat_off/on, <value> must be a real number")
    print("-if <element> is 'unit', value is either 'C' or 'F'")

def load():
    r = getSettings()
    return Settings.FromJson(r.json())

def set(inp, s):
    if(len(inp) != 3):
        print("Expected 2 arguments to command 'set'")
        helpSet()
        return
    if(inp[1] == "name"):
        s.setHouseName(inp[2])
    elif(inp[1] == "unit"):
        if(inp[2] != "C" and inp[2] != "F"):
            print("Invalid argument for 'set unit', expected C or F, got " + inp[2])
            return
        s.setUnit(inp[2])
    elif(inp[1] == "clim_on"):
        s.setClimOn(float(inp[2]))
    elif(inp[1] == "clim_off"):
        s.setClimOff(float(inp[2]))
    elif(inp[1] == "heat_on"):
        s.setHeatOn(float(inp[2]))
    elif(inp[1] == "heat_off"):
        s.setHeatOff(float(inp[2]))
    else:
        print("Invalid argument for 'set', got " + inp[1])
        return
    print(vars(s))

#this program takes input from the user to change parameters
def run():
    s = None
    print("Welcome !")
    print("Press 'help' for the list of commands")
    while(True):
        inp = input().split()
        if len(inp) == 0:
            continue
        l = inp[0]
        if l == "get":
            print(getSettings().text)
        elif l == "help" or l == "h":
            help()
        elif l == "load":
            s = load()
            print(s)
        elif l == "new":
            if(len(inp) == 1):
                s = Settings()
                print(vars(s))
            elif(len(inp) != 7):
                print("Expected 6 arguments or none to command 'new'")
            else:    
                s = Settings(inp[1], float(inp[2]), float(inp[3]), float(inp[4]), float(inp[5]), inp[6])
                print(vars(s))
        elif l == "post":
            if s is None :
                print("No settings to send")
            else :
                print(postSettings(vars(s)).text)
        elif l == "quit" or l == "q":
            break
        elif l == "see":
            if s is None :
                print("No settings loaded")
            else:
                print(vars(s))
        elif l == "set":
            if (len(inp) == 2 and inp[1] == "-h"):
                helpSet()
            elif s is None :
                print("No settings loaded")
            else:
                set(inp, s)
        else:
            print("Unknown command : " + l)
    print("Quitting application !")

run()
