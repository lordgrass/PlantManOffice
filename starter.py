"""
Author: J. Aurandt
Program Version: RW 0.0.1
Build Number: RW #00001
File Build Number: #00001
"""
import os
import importlib.util
from tkinter import *
from tkinter import ttk

class Dependency_Checker:
    def aModuleChecker():
        print('Looking for required modules')
        import_module_list = ["tkinter"]
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

        @staticmethod
        def import_addon_files(addon_path):
            imported_addons = {}
            file_list = os.listdir(addon_path)
            addon_files = [f for f in file_list if f.lower().endswith(".py")]
            for file_name in addon_files:
                module_name = os.path.splitext(file_name)[0]
                file_path = os.path.join(addon_path, file_name)
                try:
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    imported_addons[module_name] = module
                except Exception as e:
                    print(f"Error importing {module_name}: {e}")
            return imported_addons

        directory_path = "modules/" #Will be added to a json conf at some point
        imported_addons = import_addon_files(directory_path)

        print("Loaded Addons:")

        for module_name in imported_addons:
            print(module_name)

        #Buttons for included applications:
        NoteButton = ttk.Button(mainWindow, text="Notes", command=None)
        NoteButton.pack()
        mainWindow.mainloop()

Program_Launcher.bMainWindow()