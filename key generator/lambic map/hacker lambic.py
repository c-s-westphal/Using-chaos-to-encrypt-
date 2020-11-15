# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:18:57 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import random

def binary_converter (b):
     d=int(b,2)
     
     return d
 
def c_generator (U):
    c=binary_converter(U)
    
    return c

def x_generator (d):
    n=len(d)
    x=binary_converter(d)
    x=x/(2**n)
    x=x*720
    x=int(x)
    
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

def lambic_string_generator (c, A):
    N=720
    string=np.empty(N)
    A=[1,2,3,4,5,6]
    for i in range(1,N-1):
        string[i]=lambic_function(i, c, A)
        
    return string

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
    E=key[2:]
    
    return E

def lambic_hacker (d, Ep, N):
    Utry=range(1,720)
    Ub=[]
    for i in range(len(Utry)):
        Ub.append(bin(Utry[i])[2:14])
    N=int(N)
    Estor=[]
    for i in range(N):
        E=lambic_key_gen(str(Ub[i]), d, N)
        if E[0:4]==Ep:
            Estor.append(E)
    E=random.choice(Estor)
                                   
    return E

print(lambic_key_gen('111', '10101', 100))
#k=lambic_hacker('10101','1001', 100)
#print(k)


    
