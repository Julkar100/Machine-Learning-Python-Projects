# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 09:20:17 2018

@author: CodersMine
"""
"""
one way thats not the best one as it has to iterate to all the values 
and this take a lot of time to find out if we dont know the initial value

and if the initial value provided by us is too vague or large than the pswd 
then it will take forever to run and the value wont be found out whatsover 
time will be given to it

"""
import time


pswd=5298
guess=0

#ticksSTR=time.localtime(time.time()).tm_sec
ticksSTR=time.time()*1000
while(not(pswd==guess)):
    guess+=1
    print(guess)
#ticksSTP=time.localtime(time.time()).tm_sec
ticksSTP=time.time()*1000
print("guess = ",guess," Time Taken ",ticksSTP-ticksSTR)

"""
guess =  5298  Time Taken  1694.01416015625
"""
################## part 2 ######################
import numpy as np
pswd="5298"
string=[0]*len(pswd)

#ticksSTR=time.localtime(time.time()).tm_sec
ticksSTR=time.time()*1000
for i in range(len(pswd)):
    while(not(pswd[i]==str(string[i]))):
        string[i]+=1
        print(string[i])
    print("Next character searching")
    #ticksSTP=time.localtime(time.time()).tm_sec
    ticksSTP=time.time()*1000
print("\n\nthe resulting password was ",string," Time Taken ",ticksSTP-ticksSTR)    

"""
this one worked really fast as it has to iterate thorugh 
certain values only from 1-9 only 

now we are about to find the time taken in each 
of the iteration

"""
################### time ####################
import time
ticks=time.localtime(time.time())
print("Number of ticks",ticks)
"""

time.localtime(time.time())
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=5,
 tm_min=30, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
"""

import calendar

cal = calendar.month(2019, 7)
print("Here is the calendar:")
print(cal)


import time

current_milli_time = lambda: int(round(time.time() * 1000))