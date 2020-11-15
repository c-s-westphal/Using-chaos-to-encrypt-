# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:41:47 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import itertools as itr

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

def lambic_string_generator (c, N):
    N=720
    x=np.empty(N)
    x[0]=1
    lambdas=[]
    A=[1,2,3,4,5,6]
    for i in range(1,N-1):
        x[i+1]=lambic_function(x[i], c, A)
        ax1.scatter(c,x[i], color='black', alpha=0.1, edgecolors='none', label = 'Lorenz Bifurcation')
        trajectory=x[i+1]-x[i]
        if trajectory != 0:
            lambdas.append(math.log(abs(trajectory)))
    lam=stat.mean(lambdas)
    ax1.scatter(c,lam, color='red', alpha=0.5, edgecolors='none', label = 'Lyapunov Exponent')
        
        
    return x

c=range(720)

for i in range(720):
    lambic_string_generator(c[i], 5)
    
ax1.set_xlabel('c')
ax1.set_ylabel('x')
ax1.set_title('How Lyapunov Exponent Varies with Constant c for the Long orbit Lambic Map ')

