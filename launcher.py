"""
Author: J. Aurandt
Program Version: RW 0.0.1
Build Number: RW #00001
File Build Number: #00001
"""

from tkinter import *
from tkinter import ttk

class Dependency_Checker:
    def aModuleChecker():
        print('Looking for required modules')
        import_module_list = ["os", "json","tkinter"]
        modules = []
        for x in import_module_list:
            try:
                modules.append(__import__(x))
                print("Module found:", x)
            except ImportError:
                print("Error, you are missing the following dependencies:", x)

Dependency_Checker.aModuleChecker()
#Calls the above class & function before proceeding, checks for missing modules.

class Misc_Commands:
    def cChangeNotes():
        changeNoteWindow = Tk()
        changeNoteWindow.title("Change Notes")
        changeNoteWindow.geometry("800x1000")
        try:
            with open("assets/updates.txt", "r") as fullUpdateText:
                Label(changeNoteWindow, text=fullUpdateText.read()).pack()
        except FileNotFoundError:
            print("Update notes not found.")
        changeNoteWindow.mainloop()

class Program_Launcher:
    def bMainWindow():
        mainWindow = Tk()
        mainWindow.title("PlantMan Launcher")
        MenuBar = Menu(mainWindow)
        mainWindow.config(menu=MenuBar)
        file_menu = Menu(MenuBar, tearoff=False)
        file_menu.add_command(label="Change Notes", command=Misc_Commands.cChangeNotes)
        file_menu.add_command(label="Exit", command=mainWindow.destroy)
        MenuBar.add_cascade(label="File", menu=file_menu)
        mainWindow.geometry("800x800")
        mainWindow.mainloop()

Program_Launcher.bMainWindow()