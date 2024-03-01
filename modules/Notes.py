from tkinter import *
from tkinter import ttk

Module_Name = "Notes"

class NoteAppHandler:
    def aNotesWindow():
        aWindow = Tk()
        aWindow.title("Plant Man Notes:")
        aWindow.geometry("1280x720")
        nMenuBar = Menu(aWindow)
        aWindow.config(menu=nMenuBar)
        file_menu = Menu(nMenuBar, tearoff=False)
        file_menu.add_command(label="Open", command=None)
        file_menu.add_command(label="Exit", command=aWindow.destroy)
        nMenuBar.add_cascade(label="File", menu=file_menu)
        texInput = Text(aWindow, width=1240, height=720)
        texInput.pack()
        aWindow.mainloop()

NoteAppHandler.aNotesWindow()