# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:02:12 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

def lorenz_string_generator (x0, y0, N):
    s=10.
    r=28.
    b=8/3.
    N=int(N)
    x=np.empty(N)
    y=np.empty(N)
    z=np.empty(N)
    x[0]=round(x0,15)
    y[0]=round(y0,15)
    z[0]=27
    dt=0.01
    for i in range(N-1):
        x[i+1]= x[i] + ((s*(y[i]-x[i])) * dt)
        y[i+1]= y[i] + ((r*x[i]-y[i]-x[i]*z[i]) * dt)
        z[i+1]= z[i] + ((x[i]*y[i] - b*z[i]) * dt)
    
    return x

#n=range(1000)
#x=lorenz_string_generator(7.5, 7.5, 1000)
#plt.plot(n,x)
E=5   
E_str=str(E)
E_str=E_str.zfill(32)
print(E_str)