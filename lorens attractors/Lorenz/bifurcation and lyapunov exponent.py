# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:06:57 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

xmin = 1
xmax = 30
mult = (xmax - xmin)*2000

xticks = np.linspace(xmin, xmax, mult)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
zero = [0]*mult
ax1.plot(xticks, zero, 'g-')


def lorenz_xpoint_plotter (r, N):
    s=10.
    #r=28
    b=8/3.
    N=int(N)
    x=round(7.6,32)
    y=round(7.5,32)
    z=27
    dt=0.05
    lambdas=[]
    for i in range(N-1):
        x= x + ((s*(y-x)) * dt)
        y= y+ ((r*x-y-x*z) * dt)
        z= z + ((x*y - b*z) * dt)
        if i > 50:
            trajectory=s*(y-x)
            lambdas.append(math.log(abs(trajectory)))
            ax1.scatter(r,x, color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
    lam=stat.mean(lambdas)
    ax1.scatter(r,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
    
        
    return x

r=np.linspace(1,30,199)

for i in range(198):
    lorenz_xpoint_plotter(r[i], 500)
    
ax1.set_xlabel('r')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant b for the Lorens Attractor ')