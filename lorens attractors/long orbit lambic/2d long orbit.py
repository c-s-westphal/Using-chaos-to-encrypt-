# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:30:36 2020

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
    n=len(A)
    n=int(n)
    nfac=math.factorial(n)
    T1=(xi)/(nfac-1)
    T2=(c+1)/(nfac+1)
    pi_ov_2=(math.pi)/2
    F=math.sin(pi_ov_2*(T1-T2))*(nfac-1)
    val=int(F)
    
    return val

def td_lambic_function (yi, xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(yi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_td_strings_generator (cx, cy, A):
    N=720
    stringx=np.empty(N)
    stringy=np.empty(N)
    for i in range(N-1):
        stringx[i+1]=td_lambic_function(i, i, cx, A)
        stringy[i+1]=td_lambic_function(i, i, cy, A)
        
    return stringx, stringy
        
A=[1,2,3,4,5,6]

fig = plt.figure()
ax = plt.axes(projection='3d')

(xs,ys)=lambic_td_strings_generator(6, 8, A)

n=range(720)

ax.scatter3D(xs, ys, n, c=n, cmap=cm.coolwarm)

