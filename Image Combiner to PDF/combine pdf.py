# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 02:33:03 2018

@author: CodersMine
"""

from fpdf import FPDF
from PIL import Image
def makePdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) )
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page), 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")
    
    
import os
import re

whole=os.listdir()

regex=re.compile("dsd.")
matches=[string for string in whole if re.match(regex,string)]

makePdf("DSD Final",matches)