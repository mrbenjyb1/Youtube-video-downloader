
import tkinter as tk
from pytube import YouTube

def Download_Video():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(window, text='Your Video has downloaded', font='arial 20', fg="White", bg="#44617b").place(x=140, y=250)

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#44617b")
window.resizable(width=False, height=False)
window.title('YouTube Video Downloader')
window.iconbitmap("youtubeLogo.ico")

link = tk.StringVar()
tk.Label(window, text='Youtube Video Downloader', font='arial 20 bold',
         fg="White", bg="#44617b").pack()
tk.Label(window, text='Link URL', font='arial 20 bold', fg="white", bg="#44617b").place(x=250, y=60)
link_enter = tk.Entry(window, width=30, textvariable=link, font='arial 15 bold', bg="white").place(x=140, y=100)
tk.Button(window, text='DOWNLOAD VIDEO', font='arial 15 bold', fg="black", bg='white', padx=2,command=Download_Video).place(x=210, y=160)

window.mainloop()
