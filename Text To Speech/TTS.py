# to speech conversion
from gtts import gTTS
import pygame
from tkinter import *

master = Tk()
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
mytext = 'Aree bhaad me jaaaa'
 
# Language in which you want to convert
language = 'hi'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file

file = 'welcome.mp3'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(0,start=0)
master.mainloop()
print("Main Loop Over")
pygame.mixer.music.stop()
