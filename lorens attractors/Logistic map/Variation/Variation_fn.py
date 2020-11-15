# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:54:39 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_string_generator (r, x0, N):
    N=int(N)
    string=np.zeros(1200)
    string[0]=round(x0,15)
    for i in range (1200-1):
        string[i+1]=round(logistic(string[i],r),15)
        
    return string

def variance (r, x0, N):
    string=logi_string_generator(r, x0, N)
    N=int(N)
    mean=stat.mean(string)
    variance=0
    for i in range (N-1):
        variance=variance+(string[i]-mean)**2
        
    variance=variance/(N-1)
        
    return variance

numsteps=100
x=np.linspace(0.1,0.95, num=numsteps)
r=np.linspace(3.6,3.99, num=numsteps)
logi_vari=np.zeros(numsteps)

for i in range(numsteps):
    logi_vari[i]=variance(r[i], 0.5, numsteps)
    
plt.plot(r,logi_vari)