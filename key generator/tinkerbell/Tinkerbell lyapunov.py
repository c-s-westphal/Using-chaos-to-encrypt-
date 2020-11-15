# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:50:00 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

xticks = np.linspace(-0.60,-0.58,2000)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
zero = [0]*2000
ax1.plot(xticks, zero, 'g-')

def tinkerbell_string_generator (b, N):
    N=int(N)
    x=np.empty(N+1)
    y=np.empty(N+1)
    x[0]=-1.5
    y[0]=-1.5
    a=0.9
    #b=-0.6013
    c=2
    d=0.5
    lambdas=[]
    for i in range (N):
        x[i+1]=x[i]**2-y[i]**2+a*x[i]+b*y[i]
        y[i+1]=2*x[i]*y[i]+c*x[i]+d*y[i]
        if i > 150:
            ax1.scatter(b, x[i], color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
            trajectory=(2*x[i]+a)-(2*y[i]*(2*y[i]+c))+b*(2*y[i]+c)
            lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)
    ax1.scatter(b,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
    
    
    return x

b=np.linspace(-0.601,-0.58,199)

for i in range(198):
    tinkerbell_string_generator(b[i], 200)
    
ax1.set_xlabel('b')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with b for the Tinkerbell Map ')

