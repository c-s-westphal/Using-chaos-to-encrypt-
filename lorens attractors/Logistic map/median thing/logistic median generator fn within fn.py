# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:20:51 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_string_med_generator (r, x0):
    string=np.zeros(999)
    string[0]=x0
    for i in range (998):
        string[i+1]=logistic(string[i],r)
        
    m=stat.median(string)
    return m

#numsteps=1001
rs=np.linspace(3.6,3.99, num=80)
med_logi=np.zeros(80)



for i in range(80):
        med_logi[i]=logi_string_med_generator(rs[i], 0.5)

#plt.plot(rs,med_logi)

#ed_logi=logi_string_med_generator(3.9, 0.5)

#smooth


print(med_logi)
plt.plot(rs,med_logi)

