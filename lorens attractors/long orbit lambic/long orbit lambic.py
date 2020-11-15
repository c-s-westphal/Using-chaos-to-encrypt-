# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:15:08 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import itertools as itr

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
    n=len(A)
    n=int(n)
    nfac=math.factorial(n)
    T1=(xi)/(nfac-1)
    T2=(c+1)/(nfac+1)
    pi_ov_2=(math.pi)/2
    F=math.sin(pi_ov_2*(T1-T2))*(nfac-1)
    val=int(F)
    
    return val

def lambic_function (xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(xi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_string_generator (c, A):
    N=720
    string=np.empty(N)
    string[0]=1
    for i in range(1,N-1):
        string[i+1]=lambic_function(string[i], c, A)
        
        
    return string

A=[1,2,3,4,5,6]
N=720
n=range(N)
x=lambic_string_generator(176,A)
print(x)
#plt.plot(n,s)

#plt.plot(y,x)
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x')
#plt.plot(n, y, label='y')
#plt.plot(n, z, label='z')
plt.legend()

'''#3d space fig
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, z, lw=0.8)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Tinkerbell Map")

plt.show()'''

'''
#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=1')
plt.plot(n, x1, label='x0=2')
plt.legend()'''
