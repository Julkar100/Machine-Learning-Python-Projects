# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 17:23:44 2018

@author: CodersMine
"""

import pyaudio,os
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
        audio = r.listen(source)

def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")

def mainfunction():
        user = r.recognize(audio)
        print(user)
        if user == "Excel":
                excel()
        elif user == "Internet":
                internet()
        elif user == "music":
                media()
while 1:
        mainfunction()