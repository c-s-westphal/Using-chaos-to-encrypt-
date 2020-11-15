# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:40:45 2020

@author: Charlie
"""

import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_point_plotter (r, x0, N):
    N=int(N)
    last=10
    point=round(x0,15)
    for i in range (N-1):
        point=round(logistic(point,r),15)
        if i >= (N - last):
            plt.scatter(r,point,s=0.1)
        
    return point
    


numsteps=1000
x=np.linspace(0.1,0.95, num=numsteps)
r=np.linspace(3.825,3.866, num=numsteps)
logi_vari=np.zeros(numsteps)
burification=[]

for i in range(numsteps):
    burification=logi_point_plotter(r[i], 0.5, numsteps)

    


