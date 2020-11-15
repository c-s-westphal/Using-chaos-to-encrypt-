# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:32:44 2020

@author: Charlie
"""


import numpy as np
import matplotlib.pyplot as plt
dt = 0.01
num_steps = 20
xs = np.empty(num_steps+1)
x2=np.empty(num_steps+1)
r=3.72
r2=3.700001
xs[0]=0.5
x2[0]=0.5
n=range(num_steps+1)
k=0
pl=np.empty(num_steps + 1)
for i in range(num_steps):
    xs[i+1]=(r*xs[i])-(r*xs[i]*xs[i])
    xs[i+1]=round(xs[i+1],5)
    x2[i+1]=(r2*x2[i])-(r2*x2[i]*x2[i])
   # if xs[i+1]==xs[0]:
    #    k=0
    
    
              

#ac=np.correlate(xs,xs,mode='full')

plt.plot(n,xs)
plt.plot(n,x2)
plt.xlabel("Number of Iterations")
plt.ylabel("x")
print(k)

    
