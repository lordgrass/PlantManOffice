"""
Author: J. Aurandt
Date: 10/11/2023
Program V. 0.0.1
File V. 0.0.1
File Purpose: PlantMan Office, prototype.
"""

class DependencyChecker:
    def pModuleChecker():
        print('Looking for required modules')
        import_module_list = ["os", "json","tkinter","time","logging"]
        modules = []
        for x in import_module_list:
            try:
                modules.append(__import__(x))
                print("Module found:", x)
            except ImportError:
                print("Error, you are missing the following dependencies:", x)

import os
import json
import time
import logging
from pathlib import Path
from tkinter import *
from tkinter.ttk import *

#Launcher constructor:
class ConfHandler:
    def pConfGenerator():
        pDefaultConf = {
            "Conf Reset Switch": 0,
            "Logging Switch": 0,
            "Disable Update Notes on Startup": 0
        }
        with open("conf.json", "w", encoding="utf-8") as pWriteToFile:
            json.dump(pDefaultConf, pWriteToFile, ensure_ascii=False, indent=4)\
            
    def pConfWindow():
        Launcher = Tk()
        Launcher.geometry("800x800")
        Launcher.title("PlantMan Office Launcher + Settings:")
        combo_box = Combobox(Launcher, width=630, height=630).pack()
        Launcher.mainloop()
#Main window constructor:
class LaunchHandler:
    def pUpdateHistoryWindow():
        pUpdateLists = Tk()
        pUpdateLists.geometry("800x800")
        scroll_bar = Scrollbar(pUpdateLists)
        scroll_bar.pack(side=RIGHT, fill=Y)
        pUpdateLists.title("PlantMan Office Update History:")
        with open("updates.txt", "r") as pUpdateList:
            Label(pUpdateLists, text=pUpdateList.read()).pack()
        pUpdateLists.mainloop()

    def SoftwarePicker():
        pStarter = Tk()
        scroll_bar = Scrollbar(pStarter)
        scroll_bar.pack(side=RIGHT, fill=Y)
        pStarter.title("PlantMan Office app selector")
        pStarter.mainloop()
