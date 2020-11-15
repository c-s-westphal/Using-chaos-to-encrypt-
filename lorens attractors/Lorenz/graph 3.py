import numpy as np
import matplotlib.pyplot as plt

#define our functions, using def. x, y, z are our variables. s, r, b, are our
#are our parameters. Return must be used toto give back results.

def lorenz(x, y, z, s=10, r=28, b=8/3.):
    
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

#define time increments 

dt = 0.01
num_steps = 1000

#define an array which are values for x, y, z will fill. needspace for initial 
#value and then 1000 increments 

xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values, so now array has these as first value then many zeros

xs[0], ys[0], zs[0] = (-8., 8., 27.)

#now fill array 

for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)




plt.plot(xs, ys)
plt.xlabel("xs")
plt.ylabel("ys")




