# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:37:38 2020

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
    T1=labeler(A, circle_product(xi, c, A))
    T2=labeler(A, list(reversed(circle_product(xi, c, A))))
    
    return abs(T1-T2)

def lambic_function (xi, c, A):
    r=rhs(xi, c, A)
    fs=circle_product(xi, r, A)
    fv=labeler(A, fs)
    
    return fv

def lambic_string_generator (x0, c, A):
    N=1000
    string=np.empty(N)
    k=np.zeros(4)
    j=0
    string[0]=x0
    for i in range(N-1):
        string[i+1]=lambic_function(string[i], c, A)
        
        
    return string

A=[1,2,3,4,5,6]
N=1000
n=range(N)
l=np.empty(N)
x=lambic_string_generator(1,6,A)
x1=lambic_string_generator(2,6,A)
print(x1)
print(x)
#x1=lambic_string_generator(0,7, A)
#plt.plot(n,x)
#k=6
#plt.scatter(k, s)
#d=np.array()
#print()


'''for i in range(1,N):
    k=k+1
    l=lambic_string_generator (k, A)

print(l)'''
    
#plt.plot(y,x)
'''plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x')
#plt.plot(n, y, label='y')
#plt.plot(n, z, label='z')
plt.legend()'''

'''#3d space fig
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, z, lw=0.8)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Tinkerbell Map")

plt.show()'''


#2d x1 x 
plt.xlabel("Number of Iterations")
plt.ylabel("x")
plt.plot(n, x, label='x0=1')
plt.plot(n, x1, label='x0=2')
plt.legend()
    
