# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:27:46 2020

@author: Charlie
"""


import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

numsteps=999
xs=np.empty(numsteps+1,numsteps+1)
xs[0]=0.5
rs=np.linspace(3.6,4., num=numsteps)

for i in range(numsteps):
    for j in range(numsteps):
        xs[i+1]=logistic(xs[i], rs[j])
    
n=range(numsteps+1)

sci.mode(xs)

#plt.plot(n,xs)