from faulthandler import disable
from os import stat
from tkinter import *
from tkinter import ttk
from turtle import color, width

#window size
sizeX = 1000
sizeY = 600

global root
#declaring root
root = Tk()
root.geometry(f'{sizeX}x{sizeY}')
root.resizable(False,False)
root.title("yt_downloader_py")

def App():

    try:
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
        destEntry = ttk.Entry(div, width=int(sizeX))

        from main import browse_for_dest
        browse = ttk.Button(div, text='Browse', command=lambda: browse_for_dest(destEntry))

        #Spacing | Non-valid-url error lbl

        div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/3)
        div.pack_propagate(False)
        div.grid(column=0,row=1)

        pathErrorLbl = ttk.Label(div, text="Provided path is invalid!", foreground='red')

        #Enter URL

        div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/4)
        div.pack_propagate(False)
        div.grid(column=0,row=2)

        lbl = ttk.Label(div,text='Enter URL:').pack(side=LEFT, padx=5)
        urlEntry = ttk.Entry(div, width=int(sizeX/6))
        
        #ExtensionDD and AddBtn | Non-valid-url error lbl

        div = ttk.Frame(topF,relief="flat", width=sizeX-20, height=sizeY/6/4)
        div.pack_propagate(False)
        div.grid(column=0,row=3)

        urlErrorLbl = ttk.Label(div, text="Provided URL is invalid!", foreground='red')

        dd = ttk.Combobox(div, state='readonly')

        from main import add_to_list
        addBtn = ttk.Button(div,text='Add',command=lambda: add_to_list(urlEntry.get(),dd.get()))

        ext=['mp4','webm','mp3','m4a']
        dd['values'] = ext
        dd.current(0)
        
        
        #declaring bottom frame

        btmF = ttk.Frame(content, relief="solid", width=sizeX - 10, height=sizeY-(sizeY/5) -15)
        btmF.grid_propagate(False)
        btmF.pack_propagate(False)
        btmF['padding'] = 5
        btmF.grid(column=0,row=1,columnspan=3, pady=5)

        #Treeview
        global videoList
        from main import treeviewColumns

        listScroll = ttk.Scrollbar(btmF)
        listScroll.pack(side=RIGHT,fill=Y)

        videoList = ttk.Treeview(btmF, yscrollcommand=listScroll.set)
        videoList['columns'] = treeviewColumns

        headerSize = int(sizeX/7)

        videoList.column('#0', anchor=W,width=headerSize + 200)
        videoList.column('#1', anchor=W,width=headerSize)
        videoList.column('#2', anchor=W,width=headerSize - 20)
        videoList.column('#3', anchor=W,width=headerSize - 70)
        videoList.column('#4', anchor=W,width=headerSize - 70)
        videoList.column('#5', anchor=W,width=headerSize - 70)
        videoList.column('#6', anchor=W,width=headerSize - 30)
        videoList.column('#7', anchor=W,width=0, stretch=NO)

        videoList.heading("#0",text='URL', anchor=W)
        videoList.heading("#1",text='Title', anchor=W)
        videoList.heading("#2",text='Author', anchor=W)
        videoList.heading("#3",text='Length', anchor=W)
        videoList.heading("#4",text='Extension', anchor=W)
        videoList.heading("#5",text='Progress', anchor=W)
        videoList.heading("#6",text='Status', anchor=W)



        #packing
        browse.pack(side=RIGHT)
        destEntry.pack(side=LEFT, padx=5)
        addBtn.pack(side=RIGHT)
        urlEntry.pack(side=LEFT)
        dd.pack(side=RIGHT)
        pathErrorLbl.pack(side=LEFT, padx=5)
        urlErrorLbl.pack(side=LEFT, padx=5)

        videoList.pack(padx=5,pady=5, fill=Y)
    except Exception as e:
        # NULL main window - Throws error after app is closed
        print(e)

    #mainloop
    root.mainloop()
    

    