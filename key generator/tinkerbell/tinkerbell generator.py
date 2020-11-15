# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:41:39 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math

 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x0_generator (d):
    n=len(d)
    x0=0
    d=binary_converter(d)
    d=d/(2**n)
    x0=d*0.1
    x0=x0+1.4
    x0=-x0
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*0.1
    y0=y0+1.4
    y0=-y0
    
    
    return y0
    
def tinkerbell_point_generator (x0, y0, N):
    N=int(N)
    x=np.empty(N+1)
    y=np.empty(N+1)
    x[0]=round(x0,32)
    y[0]=round(y0,32)
    a=0.9
    b=-0.6013
    c=2
    d=0.5
    for i in range (N):
        x[i+1]=x[i]**2-y[i]**2+a*x[i]+b*y[i]
        y[i+1]=2*x[i]*y[i]+c*x[i]+d*y[i]
    
    return abs(x[N])
                   

def key_value_generator (U, d, N):
    x0=x0_generator(d)
    y0=y0_generator(U)
    E=tinkerbell_point_generator(x0, y0, N)
    E=abs(round(E, 32))
    
    return E

def final_binary_key_gen (U, d, N):
    E=key_value_generator(U, d, N)
    E=abs(E)/1.5
    E=E*(2**32)
    E=int(E)
    E=bin(E)
    E=E[2:]
    E=E.zfill(32)
    
    return E

#E=key_value_generator('10000', '11111', 1000)
#k=(y0_generator('0'))    
#j=x0_generator('11111') 
#print(j)
print(final_binary_key_gen ('00000', '11110', 1000))


