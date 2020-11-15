import numpy as np
import matplotlib.pyplot as plt

#define our functions, using def. x, y, z are our variables. s, r, b, are our
#are our parameters. Return must be used toto give back results.

def lorentz(xs,ys,zs,a=10., r=28., b=8/3. ):
    xdot = -a*xs+a*ys
    ydot = r*xs-ys-xs*zs
    zdot = -b*zs+xs*ys
    return(xdot, ydot, zdot)

 
#define time increments 

dt = 1
num_steps = 3000

#define an array which are values for x, y, z will fill. needspace for initial 
#value and then 1000 increments 

x = np.empty(num_steps + 1)
y = np.empty(num_steps + 1)
z = np.empty(num_steps + 1)

# Set initial values, so now array has these as first value then many zeros

x[0],y[0],z[0] = (-8.,8,27)


#now fill array 

for i in range(0,num_steps):
    xdot,ydot,zdot=lorentz(x,y,z)
    x[i + 1] = x[i]+xdot
    y[i + 1] = y[i]+ydot
    z[i+1]=z[i]+zdot
    

n=range(1,3002)

plt.plot(y, x)
plt.xlabel("Iterations")
plt.ylabel("x")





