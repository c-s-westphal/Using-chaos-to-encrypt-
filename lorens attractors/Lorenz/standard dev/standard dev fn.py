# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:04:27 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

def lorenz_string_gen (s, r, b, dt, x0, y0, z0, N):
    N=int(N)
    xs=np.empty(N)
    ys=np.empty(N)
    zs=np.empty(N)
    xs[0]=x0
    ys[0]=y0
    zs[0]=z0
    for i in range(N-1):
        xs[i + 1] = xs[i] + ((s*(ys[i]-xs[i])) * dt)
        ys[i + 1] = ys[i] + ((r*xs[i] - ys[i] - xs[i]*zs[i]) * dt)
        zs[i + 1] = zs[i] + ((xs[i]*ys[i] - b*zs[i]) * dt)
        
    return xs, ys, zs

def std (s, r, b, dt, x0, y0, z0, N):
    (xs, ys, zs)=lorenz_string_gen(s, r, b, dt, x0, y0, z0, N)
    N=int(N)
    std=stat.pstdev(xs)
        
    return std

numsteps=100
rs=np.linspace(1,80,numsteps)
lorenz_x_std=np.empty(numsteps)

for i in range(numsteps):
    lorenz_x_std[i]=std(10, rs[i], 8/3, 0.01, -4, 8, 27, 1000)
    
plt.plot(rs,lorenz_x_std)

