
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import panda as pd


#define time increments ik

dt = 0.1
num_steps = 1000

#define an array which are values for x, y, z will fill. needspace for initial 
#value and then 1000 increments 

xs = np.empty(num_steps + 1)
xt = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
yt = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)
zt = np.empty(num_steps + 1)

# Set initial values, so now array has these as first value then many zeros

xs[0], xt[0], ys[0], yt[0], zs[0], zt[0] = (1,1,1,1,1,1)
s=10.
r=28.
b=8/3.
    
n=range(1001)
#now fill array

#fig = plt.figure()
#ax = fig.gca(projection='3d') 
#k=0

for i in range(num_steps):
    xs[i + 1] = xs[i] + ((s*(ys[i]-xs[i])) * dt)
    #xs[i + 1] = round(xs[i + 1],15)
    ys[i + 1] = ys[i] + ((r*xs[i] - ys[i] - xs[i]*zs[i]) * dt)
    #ys[i + 1] = round(ys[i + 1],15)
    zs[i + 1] = zs[i] + ((xs[i]*ys[i] - b*zs[i]) * dt)
    #zs[i + 1] = round(zs[i + 1],15)
    #if xs[i]==xs[0]:
    #    k=i
        
print(xs)
#plt.plot(n,xs)
    
    
    
'''for i in range(num_steps):
    xt[i + 1] = xt[i] + ((s*(yt[i]-xt[i])) * dt)
    yt[i + 1] = yt[i] + ((r*xt[i] - yt[i] - xt[i]*zt[i]) * dt)
    zt[i + 1] = zt[i] + ((xt[i]*yt[i] - b*zt[i]) * dt)
    
    
#acx=np.correlate(xs,xs, mode='full')
#acy=np.correlate(ys,ys, mode='full')
#acz=np.correlate(zs,zs, mode='full')

n=range(num_steps+1)

#plt.plot(n, xs)
#plt.plot(n, ys )
#plt.plot(n, zs )'''
'''fig = plt.figure()
ax = plt.axes(projection='3d')

plt.xlabel("Number of Iterations")
plt.ylabel("x, y, z")
plt.plot(n, xs, label='x')
plt.plot(n, ys, label='y')
plt.plot(n, zs, label='z')
plt.legend()'''

#ax.plot3D(xs, ys, zs)

# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()



