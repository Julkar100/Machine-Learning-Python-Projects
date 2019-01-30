# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 00:30:51 2018

@author: CodersMine
"""

from textblob import TextBlob
text="python is a good language "
obj=TextBlob(text)
sentiment=obj.sentiment.polarity
print("good" if sentiment>0 else  "bad" ,sentiment)