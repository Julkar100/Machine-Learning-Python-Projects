import pygame
from tkinter import *
file = 'welcome.mp3'
master = Tk()
def stop():
    print("Stopping")
    pygame.mixer.music.stop()

def play():
    print("Not Stopping")
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(0,start=25)

def forwd():
    print("Forwd")
    pygame.mixer.music.play(0,start=5)
    
def backwd():
   print("Backwd")
   pygame.mixer.music.play(0,start=-5)
"""
there are two buttonns defined for navigation in the controller
the play button starts from specific time always not forward the song
just play from the given point again and again
"""

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(0,start=0)

playb=Button(master,text="PLAY",command=play)
stopb=Button(master,text="STOP",command=stop)
forwdb=Button(master,text="FORWARD",command=forwd)
backwdb=Button(master,text="BACKWARD",command=backwd)
playb.pack()
stopb.pack()
forwdb.pack()
backwdb.pack()

master.mainloop()
stop()

