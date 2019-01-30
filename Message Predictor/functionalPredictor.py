# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:32:24 2018

@author: CodersMine

functional predictor for essay

"""
file=open("text.txt","r")
text=file.read()
text+=" "
file.close()

file=open("text.txt","w")
file.write(text)
file.close()

def spacerem(string):
    t=""
    for word in string:
        if not(word==" "):
            t+=word
    return t

def spaceremlast(string):
    if(string[len(string)-1]==" "):
        #print("space in end")
        return string[:-1]
    else:
        return string

def dictcreate(text):
    t=""
    d={}
    l=[] 
    for word in text:    
        if not(word == " "):
            if(not(word=='.')):
                t+=word
        else:    
            l.append(t)
            t=""
    for i in range(1,len(l)):
        d.update({l[i-1]:l[i]})
    return d
    

def predict(string,d,flag):
    t=d[string]
    print(d[string])
    if flag==1:#include the predicted word
        a.append(t)
    else:
        return("")
        
        
    

def values(string):
    string=spaceremlast(string)
    flag=0
    if (string[0]==" "):
        #print("space here")
        flag=1
        return(string[1:],flag)
    else:
        flag=0
        return(string,flag)
  
a=[]
t=""
          
d=dictcreate(text)
print("Start Typing")
for i in range(100):
    try:
        string,flag=values(input())
        if(string=="exit"):
            break
        if(flag==1):
            a.append(t)
        a.append(string)
        print(d[string])
        t=d[string]
    except:        
        print("nf")

essay=" ".join(a)
file=open("predicted Message.txt",'w')
file.write(essay)
file.close()


file=open("text.txt",'a')
file.write(essay)
file.close()