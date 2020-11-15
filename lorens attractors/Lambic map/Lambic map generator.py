# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:59:46 2020

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
    for i in range(len(A)):
        output[i]=l[c][(l[xi]([i-1])]
    
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

def lambic_function (xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(xi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_string_generator (x0, c, N, A):
    N=int(N)
    string=np.empty(N)
    string[0]=x0
    for i in range(N-1):
        string[i+1]=lambic_function(string[i], c, A)
        
    return string

A=[1,2,3,4,5,6]

n=range(700)
l=lambic_string_generator(1, 680, 700, A)
print(l)
plt.plot(n,l)
#k=permutations(A)
#print(k[680][k[681][6]])


'''numsteps=500
fin=np.empty(numsteps+1)
for i in range(numsteps):
    fin[i]=lambic_function(29+i, 1, A)

n=range(numsteps+1)
plt.plot(n,fin)
print(fin)
    


A=[1,2,3,4,5,6]
fin=rhs(29,1,A)
l=(permutations(A))
print(fin)
#print(l)'''
