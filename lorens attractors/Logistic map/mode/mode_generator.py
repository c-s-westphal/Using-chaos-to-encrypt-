# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:05:39 2020

@author: Charlie
"""

import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_string_mode_generator (r, x0):
    string=np.zeros(1000)
    string[0]=x0
    for i in range (999):
        string[i+1]=round(logistic(string[i],r),15)
        
    
    m=sci.mode(string)
    return min(m)

rs=np.linspace(3.6,3.99, num=80)
mode_logi=np.zeros(80)



for i in range(80):
       mode_logi[i]=logi_string_mode_generator(rs[i], 0.3)



#mode_logi=logi_string_mode_generator(3.8, 0.5)

#smooth


plt.plot(rs,mode_logi)
#print(mode_logi)
       
