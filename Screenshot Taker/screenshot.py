# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:06:07 2018

@author: CodersMine
"""

import PIL.ImageGrab
sc=PIL.ImageGrab.grab()
sc.save('ss.jpg','JPEG')
sc.show()