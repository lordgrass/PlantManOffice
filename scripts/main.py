"""
Author: J. Aurandt
Date: 10/11/2023
Program V. 0.0.1
File V. 0.0.1
File Purpose: PlantMan Office, prototype.
Build Number: See updates.txt or launch the app by running cli.py
"""

class DependencyChecker:
    def pModuleChecker():
        print('Looking for required modules')
        import_module_list = ["os", "json","tkinter","logging", "requests"]
        modules = []
        for x in import_module_list:
            try:
                modules.append(__import__(x))
                print("Module found:", x)
            except ImportError:
                print("Error, you are missing the following dependencies:", x)

import os
import json
import requests
import logging
from pathlib import Path
from tkinter import *
from tkinter import ttk

class UpdateHandler: #Class for automatic updates by using github.
    def pUpdateManager(): #Currently disabled
        pUrl = ("https://github.com/lordgrass/PlantManOffice/archive/refs/heads/main.zip") #Current repository for latest source code zip downloads
        requests.get(pUrl)
#Launcher constructor:
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
        
    def pLauncher():
        Launcher = Tk()
        Launcher.title("PlantMan Office Launcher")
        Launcher.geometry("1920x1080")
        menubar = Menu(Launcher)
        Launcher.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=False)
        file_menu.add_command(label="Update Conf", command=ConfHandler.pConfGenerator) #To be removed in V. 1.0.0
        file_menu.add_command(label="Exit", command=Launcher.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        pFrame = Frame(Launcher, height=90, width=120)
        ttk.Button(pFrame, text="Notes", command=NoteAppHandler.pNotesWindow).pack()
        pFrame.pack()
        Launcher.mainloop()

class ConfHandler:
    def pConfGenerator(): #Should only activate when the Reset Switch is set to 1 or on first run of the program.
        pDefaultConf = {
            "Conf Reset Switch": 0,
            "Logging Switch": 0,
            "Disable Update Notes on Startup": 0,
            "Disable Automatic Program Updates": 1,
            "Window Size": 3
        }
        with open("conf.json", "w", encoding="utf-8") as pWriteToFile:
            json.dump(pDefaultConf, pWriteToFile, ensure_ascii=False, indent=4)

    def pActivateRes(): #Not implemented.
        switch={
            "3840x2160": 1,
            "2560x1440": 2,
            "1920x1080": 3, #default
            "1280x720": 4
        }

class NoteAppHandler:
    def pNotesWindow():
        nWindow = Tk()
        nWindow.title("Plant Man Notes:")
        nWindow.geometry("1280x720")
        nMenuBar = Menu(nWindow)
        nWindow.config(menu=nMenuBar)
        file_menu = Menu(nMenuBar, tearoff=False)
        file_menu.add_command(label="Exit", command=nWindow.destroy)
        nMenuBar.add_cascade(label="File", menu=file_menu)
        texInput = Text(nWindow, width=1240, height=720)
        texInput.pack()
        nWindow.mainloop()

class PMOFiles:
    def pFileManager():
        nSelector = Tk()
        nSelector.geometry("1240x720")
        nSelector.title("Plant Man Office File Manager")
        nSelector.mainloop()