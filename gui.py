from tkinter import *
from tkinter import ttk
import func

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
    content['padding'] = 5
    content.grid(column=0,row=0)

    #declaring top frame
    topF = ttk.Frame(content, relief="solid", width=sizeX - 10, height=sizeY/5)
    topF.grid_propagate(False)
    topF.pack_propagate(False)
    topF['padding'] = 5
    topF.grid(column=0,row=0,columnspan=3)

    topFheight = topF.winfo_height()
    topFwidth = topF.winfo_width()

    #Browse Path

    div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/4)
    div.pack_propagate(False)
    div.grid(column=0,row=0)

    lbl = ttk.Label(div,text='Download Path:').pack(side=LEFT, padx=5)
    destEntry = ttk.Entry(div, width=int(sizeX/8))
    browse = ttk.Button(div, text='Browse', command=lambda: func.browse_for_dest(destEntry))
    #Spacing

    div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/3)
    div.pack_propagate(False)
    div.grid(column=0,row=1)

    #Enter URL

    div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/4)
    div.pack_propagate(False)
    div.grid(column=0,row=2)

    lbl = ttk.Label(div,text='Enter URL:').pack(side=LEFT, padx=5)
    urlEntry = ttk.Entry(div, width=int(sizeX/6))
    
    #ExtensionDD and AddBtn

    div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/4)
    div.pack_propagate(False)
    div.grid(column=0,row=3)

    dd = ttk.Combobox(div, state='readonly')
    addBtn = ttk.Button(div,text='Add',command=lambda: func.add_to_list(urlEntry.get(),dd.get()))

    ext=['mp4','webm','mp3','m4a']
    dd['values'] = ext
    dd.current(0)
    
    
    #declaring bottom frame

    btmF = ttk.Frame(content, relief="solid", width=sizeX - 10, height=sizeY-(sizeY/5) -15)
    btmF.grid_propagate(False)
    btmF['padding'] = 5
    btmF.grid(column=0,row=1,columnspan=3, pady=5)

    #packing
    browse.pack(side=RIGHT)
    destEntry.pack(side=LEFT)
    addBtn.pack(side=RIGHT)
    urlEntry.pack(side=LEFT)
    dd.pack(side=RIGHT)

    #mainloop
    root.mainloop()

