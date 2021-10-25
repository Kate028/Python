from tkinter import *
import sys
from tkinter import messagebox, filedialog
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.title("Youtube Video Downloader")


def Browse_Loc():
    download_Directory = filedialog.askdirectory(
        initialdir="PATH", title="Save Video")
    loc.set(download_Directory)


Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()
loc = StringVar()
var = IntVar()

Label(root, text='Paste Video Link:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


link_enter = Entry(root, width=50, textvariable=loc).place(x=32, y=130)
Button(root, text='Browse Folder..', font='arial 10 bold', bg='gray', fg='white', command=Browse_Loc
       ).place(x=345, y=125)

g = Radiobutton(root, text="240p", variable=var, value=133).place(x=32, y=155)
l = Radiobutton(root, text="360p", variable=var, value=18).place(x=92, y=155)
m = Radiobutton(root, text="720p", variable=var, value=22).place(x=152, y=155)
h = Radiobutton(root, text="1080p", variable=var, value=137).place(x=210, y=155)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_by_itag(var.get())
    download_Folder = loc.get()
    video.download(download_Folder)
    Label(root, text='DOWNLOAD COMPLETE!!',
          font='arial 10').place(x=165, y=180)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='red', fg='white',
       padx=2, command=Downloader).place(x=180, y=230)

root.mainloop()
