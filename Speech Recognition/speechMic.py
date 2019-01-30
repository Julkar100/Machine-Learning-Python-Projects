# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 00:05:32 2018

@author: CodersMine
"""
import speech_recognition as sr
r=sr.Recognizer()

mic=sr.Microphone()

mic.list_microphone_names()

with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.2)
    print("start")
    audio=r.listen(source)
    print("stop")
    
try:    
    txt=r.recognize_google(audio)
except:
    print("Cant be recoganised")
    
print(txt)