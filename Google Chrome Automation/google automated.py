# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:13:33 2018

@author: CodersMine
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver=webdriver.Chrome('chromedriver')

target=str("avril")

driver.get("https://www.google.com/search?source=hp&ei=siGSW6enGcnkvgTRz5WADQ&q="+target+"&oq="+target+"&gs_l=psy-ab.3..0l10.1582.2944.0.105295.5.5.0.0.0.0.385.1112.0j3j1j1.5.0....0...1c.1.64.psy-ab..0.5.1107...0i131k1.0.-QgQy88gh0Y")


driver.maximize_window()
x=driver.get_screenshot_as_png()

driver.minimize_window()
file=open(target+".png",'wb')
file.write(x)
file.close()