# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:36:25 2020

@author: Charlie
"""
import numpy as np
import matplotlib.pyplot as plt
import math

numsteps=5000
x=np.empty(numsteps+1)
y=np.empty(numsteps+1)
z=np.empty(numsteps+1)
x1=np.empty(numsteps+1)
y1=np.empty(numsteps+1)
z1=np.empty(numsteps+1)

a=0.2
b=0.2
c=5.7
dt=0.01

x[0]=6
y[0]=8
z[0]=27
x1[0]=6.2
y1[0]=8
z1[0]=27
k=0

for i in range (numsteps):
    x[i+1]=x[i]+((-y[i]-z[i])*dt)
    x[i+1]=round(x[i+1],5)
    y[i+1]=y[i]+((x[i]+a*y[i])*dt)
    y[i+1]=round(y[i+1],5)
    z[i+1]=z[i]+((b+z[i]*(x[i]-c))*dt)
    z[i+1]=round(z[i+1],5)
    for j in range(i):
        if x[i] == x[j]:
            k=i
    #x1[i+1]=x1[i]+((-y1[i]-z1[i])*dt)
    #y1[i+1]=y1[i]+((x1[i]+a*y1[i])*dt)
    #z1[i+1]=z1[i]+((b+z1[i]*(x1[i]-c))*dt)
    
#acx=np.correlate(x,x,'full')
#acy=np.correlate(y,y,'full')
#acz=np.correlate(z,z,'full')

n=range(numsteps+1)
print(k)
plt.plot(n,y)

'''plt.xlabel("Number of Iterations")
plt.ylabel("x,y,z")
plt.plot(n, x, label='x')
plt.plot(n, y, label='y')
plt.plot(n, z, label='z')
plt.legend()'''

'''#3d space fig
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Rossler Map")

plt.show()'''


'''#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=6')
plt.plot(n, x1, label='x0=6.2')
plt.legend()'''
    
    

