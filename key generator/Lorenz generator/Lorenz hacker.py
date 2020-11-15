# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:31:49 2020

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
    n=len(U)
    U=binary_converter(U)
    #U=U/(2**n)
    #to make this 9 bits we make there 511 possibilities for x0 in desired range
   # U=U*511
   # U=int(U)
    U=U/4095
    x0=U*5
    x0=x0+5
    
    return x0

def y0_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    d=d*4095
    d=int(d)
    d=d/4095
    y0=d*5
    y0=y0+5
    
    return y0

def lorenz_point_generator (x0, y0, N):
    s=10.
    r=28.
    b=8/3.
    N=int(N)
    x=round(x0,12)
    y=round(y0,12)
    z=27
    dt=0.01
    for i in range(N-1):
        x= x + ((s*(y-x)) * dt)
        y= y+ ((r*x-y-x*z) * dt)
        z= z + ((x*y - b*z) * dt)
    
    return x
                   
        
#    return point_y

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=lorenz_point_generator(x0, y0, N)
    E=round(E, 12)
    
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

def lorenz_hacker (Ep, d, N):
    Utry=range(1,4095)
    Ub=[]
    for i in range(len(Utry)):
        Ub.append(bin(Utry[i])[2:12])
    N=int(N)
    Estor=[]
    for i in range(N):
        E=final_binary_key_gen(str(Ub[i]), d, N)
        if E[0:4]==Ep:
            Estor.append(E)
    E=random.choice(Estor)
                    
    return E

print(final_binary_key_gen('00101', '111', 100))
print(lorenz_hacker('0010', '111', 100))





