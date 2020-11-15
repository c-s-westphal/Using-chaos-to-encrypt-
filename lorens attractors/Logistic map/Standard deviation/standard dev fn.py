# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:48:17 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_string_generator (r, x0, N):
    N=int(N)
    string=np.zeros(N)
    string[0]=round(x0,15)
    for i in range (N-1):
        string[i+1]=round(logistic(string[i],r),15)
        
    return string

def std (r, x0, N):
    string=logi_string_generator(r, x0, N)
    N=int(N)
    mean=stat.mean(string)
    std=np.zeros(N)
    for i in range (N-1):
        std[i]=(((string[i]-mean)**2)/N)**(0.5)+(std[i-1])
        
    return std

numsteps=100
x=np.linspace(0.1,0.95, num=numsteps)
r=np.linspace(3.6,3.99, num=numsteps)
logi_std=np.zeros(numsteps)

for i in range(numsteps-1):
    logi_std=std(r[i], 0.50, numsteps)
    
plt.plot(r,logi_std)


