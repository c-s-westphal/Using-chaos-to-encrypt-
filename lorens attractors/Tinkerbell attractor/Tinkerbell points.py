# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:00:45 2020

@author: Charlie
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

N=3
a=0.9
b=-0.6013
c=2
d=0.2
x=1.8
y=0.9
'''for i in range (N-1):
    k=(x**2)-(y**2)+(a*x)+(b*y)
    j=(2*x*y)+(c*x)+(d*y)
    x=k
    y=j
    
print(x,y)'''

numsteps=1000
x1=np.empty(numsteps+1)
y1=np.empty(numsteps+1)


a=0.9
b=-0.6013
c=2
d=0.5

x1[0]=-1.4
y1[0]=-1.4

for i in range (numsteps):
    x1[i+1]=x1[i]**2-y1[i]**2+a*x1[i]+b*y1[i]
    y1[i+1]=2*x1[i]*y1[i]+c*x1[i]+d*y1[i]



n=range(numsteps+1)
plt.plot(n,x1)
print(x1,y1)