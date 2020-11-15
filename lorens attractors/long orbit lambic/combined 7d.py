# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:30:28 2020

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

def rhs2 (xi, c, A):
    n=len(A)
    n=int(n)
    nfac=math.factorial(n)
    T1=(xi)/(nfac-1)
    T2=(c+1)/(nfac+1)
    pi_ov_2=(math.pi)/2
    F=math.sin(pi_ov_2*(T1-T2))*(nfac-1)
    val=int(F)
    
    return val

def n_d_lambic_function (one_d, two_d, three_d, four_d, five_d, six_d, seven_d, c, A):
    r7=rhs(seven_d, c, A)
    r6=rhs2(six_d, c, A)
    r67=circle_product(r6, r7, A)
    r67=labeler(A, r67)
    r5=rhs(five_d, c, A)
    r56=circle_product(r5, r67, A)
    r56=labeler(A, r56)
    r4=rhs2(four_d, c, A)
    r45=circle_product(r4, r56, A)
    r45=labeler(A, r45)
    r3=rhs(three_d, c, A)
    r34=circle_product(r3, r45, A)
    r34=labeler(A, r34)
    r2=rhs2(two_d, c, A)
    r23=circle_product(r2, r34, A)
    r23=labeler(A, r23)
    rf=circle_product(one_d, r23, A)
    fv=labeler(A, rf)
    
    return fv

def lambic_nd_strings_generator (cx, cy, cz, cw, cv, cu, ct, A):
    N=720
    stringt=np.empty(N)
    stringu=np.empty(N)
    stringv=np.empty(N)
    stringw=np.empty(N)
    stringx=np.empty(N)
    stringy=np.empty(N)
    stringz=np.empty(N)
    for i in range(N-1):
        stringt[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, ct, A)
        stringu[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, cu, A)
        stringv[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, cv, A)
        stringw[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, cw, A)
        stringx[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, cx, A)
        stringy[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, cy, A)
        stringz[i+1]=n_d_lambic_function(i, i, i, i, i, i, i, cz, A)
        
    return stringt, stringu, stringv, stringw, stringx, stringy, stringz

A=[1,2,3,4,5,6]

fig = plt.figure()
ax = plt.axes(projection='3d')

(ts, us, vs, ws, xs, ys, zs)=lambic_nd_strings_generator(0, 0, 0, 0, 0, 0, 1, A)

#plt.plot(ys,xs)

n=range(720)
print(xs)
ax.scatter3D(xs, ys, vs, c=zs, cmap=cm.pink)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("String x vs String y vs String v Map")

