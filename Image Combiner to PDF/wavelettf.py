# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:52:34 2018

@author: CodersMine
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data

orignal=pywt.data.camera()
orignal=pywt.data.aero()
orignal=pywt.data.ecg()
#orignal=pywt.data.nino()
#orignal=pywt.data.ascent()
titles=['approximation','horizontal detail','vertical detail','diagonal detail']
coeffs2=pywt.dwt2(orignal,'bior1.3')
LL,(LH,HL,HH)=coeffs2
fig=plt.figure(figsize=(12,3))
for i,a in enumerate([LL,LH,HL,HH]):
    ax=fig.add_subplot(1,4,i+1)
    ax.imshow(a,interpolation="nearest",cmap=plt.cm.gray)
    ax.set_title(titles[i],fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    
fig.tight_layout()
plt.show()