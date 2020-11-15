# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:32:44 2020

@author: Charlie
"""


import numpy as np
import matplotlib.pyplot as plt
dt = 0.01
num_steps = 999
xs = np.empty(num_steps + 1)
x2=np.empty(num_steps + 1)
r=3.7
r2=3.700001
xs[0]=0.5
x2[0]=0.5
n=range(1,2000)
pl=np.empty(num_steps + 1)
for i in range(num_steps):
    xs[i+1]=(r*xs[i])-(r*xs[i]*xs[i])
    x2[i+1]=(r2*x2[i])-(r2*x2[i]*x2[i])
    
              

ac=np.correlate(xs,xs,mode='full')

plt.plot(n,ac)

    
