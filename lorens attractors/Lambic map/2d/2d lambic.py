# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:25:04 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
import scipy
import itertools as itr
from mpl_toolkits.mplot3d import Axes3D

# Python function to print permutations of a given list 
def permutations(A): 
  
    # If lst is empty then there are no permutations 
    if len(A) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(A) == 1: 
        return [A] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(A)): 
       m = A[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = A[:i] + A[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutations(remLst): 
           l.append([m] + p) 
    return l

def circle_product (xi, c, A):
    l=permutations(A)
    #output=np.empty(len(A))
    output=[0,0,0,0,0,0]
    c=int(c)
    xi=int(xi)
    C=l[c]
    Xi=l[xi]
    for i in range(len(A)):
        output[i]=C[Xi[i]-1]
    
    return output

def labeler (A, Xi):
    l=permutations(A)
    for i in range(math.factorial(len(A))):
        if l[i]==Xi:
            return i
        
def rhs (xi, c, A):
    T1=labeler(A, circle_product(xi, c, A))
    T2=labeler(A, list(reversed(circle_product(xi, c, A))))
    
    return abs(T1-T2)

def td_lambic_function (yi, xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(yi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_td_strings_generator (x0, y0, cx, cy, A):
    N=1000
    stringx=np.empty(N)
    stringx[0]=x0
    stringy=np.empty(N)
    k=0
    for i in range(N-1):
        stringx[i+1]=td_lambic_function(stringx[i], stringy[i], cx, A)
        stringy[i+1]=td_lambic_function(stringy[i], stringx[i], cy, A)
        
    return stringx, stringy

A=[1,2,3,4,5,6]

n=range(1000)

'''fig = plt.figure()
ax = plt.axes(projection='3d')







#ax.plot3D(xs, ys, n, 'gray')
ax.scatter3D(xs, ys, n, c=n, cmap=cm.coolwarm)'''

(x, y)=lambic_td_strings_generator(431, 52, 134, 55, A)
#(x,y)=lambic_td_strings_generator(3, 12, 54,54, A)
#(x1, ys1)=lambic_td_strings_generator(2, 6, 6, A)
#plt.plot(n,ys)
#Axes3D.plot(xs,ys,n)
#3d plot
#print(k)
'''fig = plt.figure()
ax = fig.gca(projection='3d')
# Plot the surface.
ax.plot_surface(xs, ys, n, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()'''

'''#plt.plot(y,x)
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, xs, label='x0=1 where cx=6')
plt.plot(n, x1, label='x0=2 where cx=6')
#plt.plot(n, z, label='z')
plt.legend()'''

#print(xs)'

#3d space fig
'''fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(xs, ys, n, lw=0.8)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Multidimensional Lambic Map")

plt.show()'''


#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x')
plt.plot(n, y, label='y')
plt.legend()

