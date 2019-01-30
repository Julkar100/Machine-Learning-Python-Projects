# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 17:32:40 2018

@author: CodersMine


The adjust_for_ambient_noise() method reads 
the first second of the file stream and calibrates the recognizer
 to the noise level of the audio. Hence, that portion of the stream 
 is consumed before you call record() to capture the data.
You can adjust the time-frame that adjust_for_ambient_noise() 
uses for analysis with the duration keyword argument. This argument 
takes a numerical value in seconds and is set to 1 by default.
 Try lowering this value to 0.5.
"""


import speech_recognition as sr

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate=48000
chunk_size=2048

r= sr.Recognizer()

device_id=1
mic_list = sr.Microphone.list_microphone_names()

for i,microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
        
para=[]
text=" "

while(not text=="stop"):
     with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source,duration=0.1)
        print("Say : ")
        audio=r.listen(source)
        
        try:
            text=r.recognize_google(audio)
            print(text)
            para.append(text)
        except sr.UnknownValueError:
            print("Cant Understand What you are saying")
        except sr.RequestError as e:
            print("Could not request result from GOOGLE {0}".format(e))
            
file=open("Speech.txt",'w')
for i in range(len(para)):
    file.write(para[i]+"\n")
file.close()