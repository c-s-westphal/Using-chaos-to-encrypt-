# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:49:13 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

xmin = 0
xmax = 2
mult = (xmax - xmin)*2000

xticks = np.linspace(xmin, xmax, mult)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
zero = [0]*mult
ax1.plot(xticks, zero, 'g-')

def henon_xpoint_generator (a , N):
    N=int(N)
    x=1
    y=1.1
    #a=0.68
    b=0.3
    lambdas=[]
    for i in range(N-1):
        x=1-(a*x*x)+y
        y=b*x
        if i > 50:
            trajectory=2*a*x
            lambdas.append(math.log(abs(trajectory)))
            ax1.scatter(a,x, color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
    lam=stat.mean(lambdas)
    ax1.scatter(a,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
    
    return x

a=np.linspace(0.01,2,199)

for i in range(198):
    henon_xpoint_generator(a[i], 100)
    
ax1.set_xlabel('r')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant b for the Henon Attractor ')