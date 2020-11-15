# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:39:08 2020

@author: Charlie
"""

import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math



xticks = np.linspace(0.01, 0.9, 2000)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
zero = [0]*2000
ax1.plot(xticks, zero, 'g-')

def ikeda_point_generator (u, N):
    N=int(N)
    x=9
    y=8
    t=0
    #u=0.918
    lambdas=[]
    for i in range(N-1):
        t=0.4-(6/(1+x*x+y*y))
        x=1+u*(x*math.cos(math.degrees(t))-y*math.sin(math.degrees(t)))
        y=u*(x*math.sin(math.degrees(t))+y*math.cos(math.degrees(t)))
        #trajectory=(12*x/(x**2+y**2+1)**2)*u*math.cos(t)
        #lambdas.append(math.log(abs(trajectory)))
        if i > 50:
            ax1.scatter(u,x, color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
            trajectory=u*math.cos(t)+(u*x*math.sin(t))*(12*x/(x**2+y**2+1)**2)
            lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)+1
    ax1.scatter(u,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
    
    return x

u=np.linspace(0.01,0.9,199)

for i in range(198):
    ikeda_point_generator(u[i], 100)
    
ax1.set_xlabel('u')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant u for the Ikeda Attractor ')