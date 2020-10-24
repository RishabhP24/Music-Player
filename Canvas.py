import os
import pygame
from mutagen.id3 import ID3
from pygame import mixer

from tkinter import *
from tkinter.ttk import *

from tkinter.filedialog import askdirectory
import random

root = Tk()
root.geometry('400x400+200+50')
root.title("Music Place")
root.iconbitmap("player.ico")
root.resizable(False,False)


listofsongs = []


index=0

v = StringVar()
songlabel = Label(root, textvariable=v, width=50)



w= Scale(from_=0, to=100)
w.pack()

def playsong(event):
    pygame.mixer.music.play()
    pygame.mixer.unpause()

    updatelabel()


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def randomsong(event):

    x = random.randint(0, len(listofsongs))
    pygame.mixer.music.load(listofsongs[x])
    pygame.mixer.music.play()
    updatelabel(x)



def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def updatelabel(loc=None):
    global index
    if loc is not None:
        v.set(listofsongs[loc])
    else:
        v.set(listofsongs[index])


def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            listofsongs.append(files)
            print(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])


directorychooser()

label = Label(root, text=f"Music List-{len(listofsongs)}Songs")
label.pack()


listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()


for items in listofsongs:
    listbox.insert(0,items)

listofsongs.reverse()


playbutton = Button(root, text="Play")
playbutton.pack()

nextbutton = Button(root,text="Next Song")
nextbutton.pack()

randombutton = Button(root,text="Random Song")
randombutton.pack()

previousbutton = Button(root,text="Previous Song")
previousbutton.pack()

stopbutton = Button(root,text="Stop")
stopbutton.pack()

playbutton.bind("<Button-1>", playsong)
nextbutton.bind("<Button-1>", nextsong)
randombutton.bind("<Button-1>", randomsong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)

songlabel.pack()

root.mainloop()