# Import libraries tkinter, pytube
# pytube is a python library for downloading YouTube Videos.
# Create display window
# Create field to enter link
# Create function to start downloading

from tkinter import *
from pytube import YouTube

# now lets create display window
window = Tk()  # Tk() used to initialize tkinter
window.geometry('600x350')  # set width x height
window.resizable(0,0) # set fixed size of window
window.title("Youtube video downloader") # used to give title of window

# Create Field to Enter Link
link = StringVar()  # store yt link that user enter
Label(window, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(window,textvariable = link, width = 50).place(x = 32, y = 90)

# Function to Start Downloading video
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
window.mainloop() # method mainloop() tells Python to run the Tkinter event loop