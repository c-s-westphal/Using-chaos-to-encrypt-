# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:54:22 2020

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

def rossler_point_generator (b,N):
    N=int(N)
    z=27
    x=0.5
    y=0.5
    a=0.2
    #b=0.2
    c=5.7
    dt=0.01
    lambdas=[]
    for i in range (N-1):
        x=x+((-y-z)*dt)
        y=y+((x+a*y)*dt)
        z=z+((b+z*(x-c))*dt)
        if i > 50:
            ax1.scatter(b,x, color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
            trajectory=-y-z
            lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)
    ax1.scatter(b,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
        
    return x

b=np.linspace(0.01,2,199)

for i in range(198):
    rossler_point_generator(b[i], 100)
    
ax1.set_xlabel('u')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with b for the Rossler Attractor ')