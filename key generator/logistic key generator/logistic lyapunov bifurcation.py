# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:19:20 2020

@author: Charlie
"""

import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

xticks = np.linspace(0.01, 2.2, 2000)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
zero = [0]*2000
ax1.plot(xticks, zero, 'g-')

def logistic (x, r):
    xdot=x+r-x**2
    
    return xdot

def logi_point_generator (r, N):
    N=int(N)
    x=0.5
    lambdas=[]
    for i in range (N-1):
        x=logistic(x,r)
        if i > 50:
            ax1.scatter(r,x, color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
            trajectory=1-2*x
            lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)
    ax1.scatter(r,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
        
    return x

r=np.linspace(0.01,2.2,199)

for i in range(198):
    logi_point_generator(r[i], 100)
    
ax1.set_xlabel('u')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant r for the Logistic Map ')