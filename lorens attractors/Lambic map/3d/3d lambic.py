# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:55:01 2020

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

def three_d_lambic_function (one_d, two_d, three_d, c, A):
    r1=rhs(one_d, c, A)
    r2=rhs(two_d, c, A)
    rf=circle_product(r1, r2, A)
    r=labeler(A, rf)
    fs=circle_product(three_d, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_td_strings_generator (x0, y0, z0, cx, cy, cz, A):
    N=1000
    stringx=np.empty(N)
    stringy=np.empty(N)
    stringz=np.empty(N)
    stringx[0]=x0
    stringy[0]=y0
    stringz[0]=z0
    for i in range(N-1):
        stringx[i+1]=three_d_lambic_function(stringx[i], stringy[i], stringz[i], cx, A)
        stringy[i+1]=three_d_lambic_function(stringy[i], stringz[i], stringx[i], cy, A)
        stringz[i+1]=three_d_lambic_function(stringz[i], stringx[i], stringy[i], cz, A)
        
    return stringx, stringy, stringz

A=[1,2,3,4,5,6]



(xs,ys, zs)=lambic_td_strings_generator(1,2,1,1, 1, 1, A)
n=range(1000)
#plt.plot(n,xs)

#print(xs)

fig = plt.figure()
ax = plt.axes(projection='3d')

(xs,ys, zs)=lambic_td_strings_generator(1,2,1,1, 1, 1, A)
n=range(1000)

#ax.plot3D(xs, ys, n, 'gray')
ax.scatter3D(xs, ys, zs, c=zs, cmap=cm.coolwarm)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3-Dimensional Lambic Map")
#print(circle_product(11,13,[1,2,3,4,5,6]))
#plt.plot(y,x)'''

'''plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, xs, label='x')
plt.plot(n, ys, label='y')
plt.plot(n, zs, label='z')
plt.legend()'''

#print(xs)'

'''#3d space fig
fig = plt.figure()
ax = fig.axes(projection='3d')

(xs,ys, zs)=lambic_td_strings_generator(1,2,1,1, 1, 1, A)

ax.scatter(xs, ys, zs, c=n, cmap=cm.coolwarm)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3-Dimensional Lambic Map")

plt.show()'''

'''
#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=1')
plt.plot(n, x1, label='x0=2')
plt.legend()'''