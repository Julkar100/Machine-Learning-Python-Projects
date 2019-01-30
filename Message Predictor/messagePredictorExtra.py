# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:45:00 2018

@author: CodersMine

creating an essay from net 
then making groups of word of two 
if any one of the word is used then predict the next one
"""

text="The word apple comes from the latin word pomum. which means fruit in general. Then known as pome because of it's tiny seeds. Before Christianity became the mainstream religion of the roman empire, apple was malum in latin which means melon. However after Christianity became the dominate religion, Apple became the Fruit of the fruit. Mainly because of the story of Adams and Eves. Nobody know why the fruit Adam was tempted with wasn't a kiwi. Why the gardan of Eden didn't grow pears. The tree of knowledge simply grew apples. Therefore apples have a great significant in Christianity. "

t=""
l=[]
d={}
for word in text:    
    if not(word == " "):
        if(not(word=='.')):
            t+=word
    else:    
        l.append(t)
        t=""
        
for i in range(1,len(l)):
    d.update({l[i-1]:l[i]})
    
a=[]
t=""  
c=""
for i in range(100):
    t=spaceremlast(input())
    if t=="exit":
        break
    a.append(t)
    try:
        
        print(d[t])
       
        print("enter to accept space to ignore")
        c=input()
        if not (c==" "):
            print("\t\t\taffirmative")
            a.append(d[t])
        else:
            print("\t\t\tignored")
    except:
        print("n.f.")
        
essay=" ".join(a)

file=open("predicted Message.txt",'w')
file.write(essay)
file.close()

def spacerem(string):
    t=""
    for word in string:
        if not(word==" "):
            t+=word
    return t

def spaceremlast(string):
    if(string[len(string)-1]==" "):
        print("space in end")
        return string[:-1]
    else:
        return string
