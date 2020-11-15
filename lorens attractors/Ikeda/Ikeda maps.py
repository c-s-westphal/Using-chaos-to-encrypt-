# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:41:13 2020

@author: Charlie
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#ikeda

numsteps=1000
x=np.empty(numsteps+1)
y=np.empty(numsteps+1)
t=np.empty(numsteps+1)

x[0]=9
y[0]=9

x1=np.empty(numsteps+1)
y1=np.empty(numsteps+1)
t1=np.empty(numsteps+1)

x1[0]=9.01
y1[0]=9
u=0.918
k=0

for i in range(numsteps):
    t[i]=0.4-(6/(1+x[i]*x[i]+y[i]*y[i]))
 
    x[i+1]=1+u*(x[i]*math.cos(math.degrees(t[i]))-y[i]*math.sin(math.degrees(t[i])))
    
    y[i+1]=u*(x[i]*math.sin(math.degrees(t[i]))+y[i]*math.cos(math.degrees(t[i])))
   
        
    t1[i]=0.4-(6/(1+x1[i]*x1[i]+y1[i]*y1[i]))
    x1[i+1]=1+u*(x1[i]*math.cos(math.degrees(t1[i]))-y1[i]*math.sin(math.degrees(t1[i])))
    y1[i+1]=u*(x1[i]*math.sin(math.degrees(t1[i]))+y1[i]*math.cos(math.degrees(t1[i])))
    

#acx=np.correlate(x,x,'full')
#acy=np.correlate(y,y,'full')

n=range(1001)


#plt.plot(n,x)
#plt.plot(n,x)

#print(x,y)
#2d x v y
'''plt.xlabel("Number of Iterations")
plt.ylabel("x,y, t")
plt.plot(n, x, label='x')
plt.plot(n, y, label='y')
plt.plot(n, t, label='t')
plt.legend()'''

'''#3d space fig
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, t)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("t Axis")
ax.set_title("Ikeda Map")

plt.show()'''


#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=9')
plt.plot(n, x1, label='x0=9.1')
plt.legend()
   
    




