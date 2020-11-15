# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:35:59 2020

@author: Charlie
"""
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

numsteps=5000
x=np.empty(numsteps+1)
y=np.empty(numsteps+1)
x1=np.empty(numsteps+1)
y1=np.empty(numsteps+1)

a=0.9
b=-0.57
c=2
d=0.5

x[0]=-1.4
y[0]=-1.4
x1[0]=-1.3
y1[0]=-1.3
k=0
for i in range (numsteps):
    x[i+1]=x[i]**2-y[i]**2+a*x[i]+b*y[i]
    #x[i+1]=round(x[i+1],15)
    y[i+1]=2*x[i]*y[i]+c*x[i]+d*y[i]
    #y[i+1]=round(y[i+1],15)
    x1[i+1]=x1[i]**2-y1[i]**2+a*x1[i]+b*y1[i]
    y1[i+1]=2*x1[i]*y1[i]+c*x1[i]+d*y1[i]
    #for j in range(i):
     #   if x[i] == x[j]:
      #      k=i
    
#acx=np.correlate(x,x,'full')
#acy=np.correlate(y,y,'full')
#acz=np.correlate(z,z,'full')

n=range(numsteps+1)
#plt.plot(n,x)
#print(x,y)

#plt.plot(y,x)
plt.xlabel("Number of Iterations")
plt.ylabel("x,y,z")
plt.plot(n, x, label='x0=-1.3')
plt.plot(n, x1, label='x0=-1.4')
#plt.title('Possible Different Tinkerbell Graph with Different x0')
#plt.plot(n, z, label='z')
plt.legend()

#3d space fig
'''fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, n, lw=1)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Tinkerbell Map")

plt.show()'''

'''
#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=-1.5')
#plt.plot(n, x1, label='x0=-1.500000001')
plt.legend()'''

