"""
Author: J. Aurandt
Date: 10/11/2023
Program V. 0.0.1
File V. 0.0.1
File Purpose: Office Demo Program
"""

class DependencyChecker:
    def pModuleChecker():
        print('Looking for required modules')
        import_module_list = ["time", "os", "tkinter", "datetime", "time"]
        modules = []
        for x in import_module_list:
            try:
                modules.append(__import__(x))
                print("Module found:", x)
            except ImportError:
                print("Error, you are missing the following dependencies:", x)

import os
#import time
from tkinter import *
from tkinter.ttk import *
#import datetime

class ConfHandler:
    def pConfGenerator():
        print("Looking for Configuration File.")
        if os.path.isfile("Configuration.txt"):
            print("Configuration file found, proceding.")
        else:
            print("Configuration file not found. Generating default file.")
            conf = open("Configuration.txt", "w")
            conf.writelines(["#Do not edit this configuration file before reading the manual.", "\npLogFile = 0"])
            conf.close
#Log switch, looks in configuration.txt 0 = off 1 = on (Currently not functional.)
    def pConfLogFile():
        pLogging = input("Do you wish to set up logging? this would be for debug purposes only. \nY for yes, N for no. ")
        if os.path.isfile("Log.txt"):
            print("Logging has already been set up, proceeding.")
        else:
            print(pLogging)
            while True:
                if pLogging == str("Y"):
                    print("Turning on debug logging, would you like to save this setting? Please enter Y or N. ")
                    while True:
                        pLogging2 = input("")
                        print(pLogging2)
                        if pLogging2 == str("Y"):
                            print("Saving Preference.")
                            pLogFile = open("Log.txt", "w")
                            pLogFile.writelines(["Logging has been enabled."])
                            conf.writelines(["#Do not edit this configuration file before reading the manual.", "\npLogFile = 1"])
                            conf.close
                        else:
                            break
                elif pLogging == str("N"):
                    print("You have chosen to use this software with debug logging turned off. Proceeding:")
                    break
                else:
                    print("Please enter Y or N, you enetered: ", pLogging)
                    continue
#Main window constructor:
class LaunchHandler:
    def pUpdateHistoryWindow():
        Launcher = Tk()
        Launcher.geometry("800x800")
        scroll_bar = Scrollbar(Launcher)
        scroll_bar.pack(side=RIGHT, fill=Y)
        Launcher.title("PlantMan Office Update History:")
        with open("updates.txt", "r") as pUpdateList:
            Label(Launcher, text=pUpdateList.read()).pack()
        Launcher.mainloop()

    def pSoftwarePicker():
        pStarter = Tk()
        pStarter.geometry("1920x1080")
        scroll_bar = Scrollbar(pStarter)
        scroll_bar.pack(side=RIGHT, fill=Y)
        pStarter.title("PlantMan Office app selector")
        pStarter.mainloop()
