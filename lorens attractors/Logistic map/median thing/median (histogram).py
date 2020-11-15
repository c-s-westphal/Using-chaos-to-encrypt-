# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:17:19 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

numsteps=999
xs=np.empty(numsteps+1)
xs[0]=0.5

for i in range(numsteps):
    xs[i+1]=logistic(xs[i], 3.7)
    
n=range(numsteps+1)

plt.plot(n,xs)

print(stat.median(xs))

