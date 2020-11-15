# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:11:19 2020

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
    x0=d*10
    x0=x0+1
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*10
    y0=y0+1
    
    return y0

def rossler_point_generator (x0, y0, N):
    N=int(N)
    x=round(x0,15)
    y=round(y0,15)
    z=27
    a=0.2
    b=0.2
    c=5.7
    dt=0.01
    for i in range (N-1):
        x=x+((-y-z)*dt)
        y=y+((x+a*y)*dt)
        z=z+((b+z*(x-c))*dt)
    
    return x
                   

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=rossler_point_generator(x0, y0, N)
    E=round(E, 7)
    
    return E

def final_binary_key_gen (U, d, N):
    E=key_value_generator(U, d, N)
    E=E*(10**7)
    E=int(E)
    E=bin(E)
    
    return E

def hamming_distance(x, y):
    dy=len(y)
    dx=len(x) 
    hd=0
    for i in range(2, dx):
        if dx==dy and x[i] != y[i]:
                hd=hd+1
                
    return(hd)

E=final_binary_key_gen('0', '0', 1000)
    
print(E) 

