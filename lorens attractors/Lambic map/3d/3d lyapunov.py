# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:10:10 2020

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

xticks = np.linspace(0.01, 360, 2000)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)
zero = [0]*2000
ax1.plot(xticks, zero, 'g-')

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

def lambic_td_strings_generator (cx, N):
    stringx=np.empty(N)
    stringy=np.empty(N)
    stringz=np.empty(N)
    stringx[0]=3
    stringy[0]=1
    stringz[0]=2
    A=[1,2,3,4,5,6]
    cz=12
    cy=65
    lambdas=[]
    for i in range(N-1):
        stringx[i+1]=three_d_lambic_function(stringx[i], stringy[i], stringz[i], cx, A)
        stringy[i+1]=three_d_lambic_function(stringy[i], stringz[i], stringx[i], cy, A)
        stringz[i+1]=three_d_lambic_function(stringz[i], stringx[i], stringy[i], cz, A)
        ax1.scatter(cx,stringx[i], color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
        trajectory=stringx[i+1]-stringx[i]
        if trajectory != 0:
            lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)
    ax1.scatter(cx,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
        
    return stringx, stringy, stringz

c=range(360)

for i in range(360):
    lambic_td_strings_generator(c[i], 30)
    
ax1.set_xlabel('c')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant cx for the 3d Lambic Map ')

