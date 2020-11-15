# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:10:58 2020

@author: Charlie
"""
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import math
import scipy
import itertools as itr

def binary_converter (b):
     d=int(b,2)
     
     return d
 
def c_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    c=int(d*720)
    
    return c

def x_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    x=int(U*720)
    
    return x

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

def lambic_function (xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(xi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_point_generator (cx, x0, N):
    A=[1,2,3,4,5,6]
    pointx=x0
    N=int(N)
    for i in range(N-1):
        pointx=lambic_function(pointx, cx, A)
           
    return pointx

def lambic_key_gen (U, d, N):
    c=c_generator(d)
    x=x_generator(U)
    key=lambic_point_generator(c, x, N)
    #key=key*10
    key=bin(key)
    E=key[2:10]
    
    return E


    



E=lambic_key_gen('100001010','1010111', 2)
print(E)

