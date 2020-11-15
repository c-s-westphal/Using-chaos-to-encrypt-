# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:13:32 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math
import random

 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x0_generator (U):
    #n=len(U)
    U=binary_converter(U)
    #U=U/(2**n)
    #to make this 9 bits we make there 511 possibilities for x0 in desired range
    #U=U*511
    #U=int(U)
    U=U/4095
    x0=U*1
    x0=x0+0.1
    x0=-x0
    
    return x0

def y0_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    d=d*4095
    d=int(d)
    d=d/4095
    y0=d*1
    y0=y0+0.1
    y0=-y0
    
    return y0
    
def tinkerbell_point_generator (x0, y0, N):
    N=int(N)
    x=np.empty(N+1)
    y=np.empty(N+1)
    x[0]=round(x0,12)
    y[0]=round(y0,12)
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
    E=abs(E)
    
    return E

def final_binary_key_gen (U, d, N):
    v_raw=key_value_generator(U, d, N)
    v_int=abs(int(v_raw))
    v_bin=bin(v_int)
    n=len(v_bin)
    division_factor=2**n
    E=(v_raw/division_factor)*(2**12)
    E=abs(int(E))
    E=bin(E)
    E=E[2:]
    E=E.zfill(12)
    
    return E

def tinkerbell_hacker (Ep, d, N):
    Utry=range(1,4095)
    Ub=[]
    for i in range(len(Utry)):
        Ub.append(bin(Utry[i])[2:14])
    N=int(N)
    Estor=[]
    for i in range(N):
        E=final_binary_key_gen(str(Ub[i]), d, N)
        if E[0:4]==Ep:
            Estor.append(E)
    E=random.choice(Estor)
                                   
    return E

print(final_binary_key_gen('0010', '00111', 100))
print(tinkerbell_hacker('0000', '00111', 100))

