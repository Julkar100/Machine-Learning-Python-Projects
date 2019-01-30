# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:15:51 2018

@author: CodersMine
"""

import speech_recognition as sr
r = sr.Recognizer()

harvard=sr.AudioFile('harvard.wav')
with harvard as source:
    audio=r.record(source)
    

r.recognize_sphinx(audio,show_all=True)
r.recognize_google(audio)