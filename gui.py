from tkinter import *
from tkinter import ttk

#window size
sizeX = 800
sizeY = 600

def App():

    #declaring root
    root = Tk()
    root.geometry(f'{sizeX}x{sizeY}')
    root.resizable(False,False)
    root.title("yt_downloader_py")

    #declaring content frame
    content = ttk.Frame(root)
    content.grid(column=0,row=0)

    #declaring top frame
    topF = ttk.Frame(content, relief="ridge")
    topF.grid(column=0,row=0,rowspan=3)

    #mainloop
    root.mainloop()
