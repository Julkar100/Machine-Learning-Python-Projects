# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:38:31 2019

@author: CodersMine
"""

import re
pattern =r"spam"

if re.match(pattern,"spamspamspam"):
    print("match")
else:
    print("No Match")
    
    
if re.search(pattern,"eggs and spam are friends"):
    print("got a match")
else:
    print("no match")
    
print(re.findall(pattern,"eggs spam and spam are spam"))


match=re.search(pattern,"eggs spam and spam souce")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    
    
str="My name is David. Hi david"
pattern=r"david"
newStr=re.sub(pattern,"Amy",str)
print(newStr)

#//Meta characters

str=r"I am \r \a \w"
pattern=r"gr.y"

if re.match(pattern,r"gray"):
    print("Match 1")
if re.match(pattern,"grey"):
    print("Match 2")
if re.match(pattern,"blue"):
    print("Match 3")
    
str="please contact vermavinay982@gmail.com for assitance"

pattern=r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match=re.search(pattern,str)
if match:   
    print(match.group())
    
"""
\d digits
\s spaces
\w word characters
"""

pattern=r"gr(a|e)y"
str="gray"
str2="grey"

if re.match(pattern,str):
    print("matches")
if re.match(pattern,str2):
    print("this too matches")
    
import this 
"""
Zen of python the principles and philosophies that are helpful in understanding and using the language effectively 
"""
