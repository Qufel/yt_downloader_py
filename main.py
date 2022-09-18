from logging import root
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import gui

global isPathValid
global isUrlValid
global folderPath
global treeviewColumns

treeviewColumns = ('URL','Title','Author','Length','Extension','Progress','Status')

def browse_for_dest(entry):
    print('Browsing for destination...')
    folderPath = filedialog.askdirectory()
    entry.delete(0,END)
    entry.insert(0,folderPath)
    print(folderPath)
    return

def add_to_list(url,ext):
    print('Adding video to list...')

    print(f'{url}.{ext}')
    return

#runs gui
gui.App()


