# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:38:58 2020

@author: Charlie
"""


import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

N=1000

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_string_generator (r, x0):
    string=np.zeros(N)
    #string[0]=round(x0,15)
    string[0]=x0
    for i in range (N-1):
        #string[i+1]=round(logistic(string[i],r),15)
        string[i+1]=logistic(string[i],r)
        
    return string

#logi=logi_string_generator(round(3.84,15), 0.5)
x=logi_string_generator(3.7,0.8)
x1=logi_string_generator(3.7, 0.800000001)

n=range(N)

#plt.plot(n,logi)

#2d x v y
'''plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, logi, label='x')
#plt.plot(n, y, label='y')
#plt.plot(n, t, label='t')
plt.legend()'''

'''#3d space fig
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, t)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("t Axis")
ax.set_title("Ikeda Map")

plt.show()
'''

#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=0.8')
plt.plot(n, x1, label='x0=0.800000001')
plt.legend()

