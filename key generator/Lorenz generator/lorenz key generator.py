# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:41:41 2020

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
    d=binary_converter(d)
    d=d/(2**n)
    
    x0=d*5
    x0=x0+5
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*5
    y0=y0+5
    
    return y0

def lorenz_point_generator (x0, y0, N):
    s=10.
    r=28.
    b=8/3.
    N=int(N)
    x=round(x0,32)
    y=round(y0,32)
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
    E=round(E, 32)
    
    return E

def final_binary_key_gen (U, d, N):
    E=key_value_generator(U, d, N)
    E=abs(E)/20
    E=E*(2**32)
    E=int(E)
    E=bin(E)
    E=E[2:]
    E=E.zfill(32)
    
    return E

E=final_binary_key_gen('00000', '00111', 1000)
    
print(E) 
print(len(E))

