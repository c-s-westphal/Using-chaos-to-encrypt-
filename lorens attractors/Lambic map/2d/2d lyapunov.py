# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:53:26 2020

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

xticks = np.linspace(0.01, 720, 2000)

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

def td_lambic_function (yi, xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(yi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_td_strings_generator (cx, N):
    cy=360
    x=np.empty(N)
    x[0]=1
    y=np.empty(N)
    y[0]=1
    A=[1,2,3,4,5,6]
    lambdas=[]
    for i in range(N-1):
        x[i+1]=td_lambic_function(x[i], y[i], cx, A)
        y[i+1]=td_lambic_function(y[i], x[i], cy, A)
        ax1.scatter(cx,x[i], color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
        trajectory=x[i+1]-x[i]
        lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)
    ax1.scatter(cx,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
        
    return x, y

c=range(720)

for i in range(720):
    lambic_td_strings_generator(c[i], 50)
    
ax1.set_xlabel('c')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant c for the 2d Lambic Map ')


