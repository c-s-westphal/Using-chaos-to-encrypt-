# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:07:51 2020

@author: Charlie
"""

import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x0_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    x0=d+0.5
    
    return x0

def a_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    U=U*0.97
    a=U+0.4
    
    return a

def henon_point_generator (x0, y0, a, b, N):
    N=int(N)
    x=round(x0,15)
    y=round(y0,15)
    for i in range(N-1):
        x=1-(a*x*x)+y
        y=b*x
    
    return x
                   
        
#    return point_y

def key_value_generator (U, d, y0, b, N):
    x0=x0_generator(U)
    a=a_generator(d)
    (E)=henon_point_generator(x0, y0, a, b, N)
    E=round(E, 7)
    
    return E

def final_binary_key_gen (U, d, y0, b, N):
    E=key_value_generator(U, d, y0, b, N)
    E=E*(10**7)
    E=int(E)
    E=bin(E)
    
    return E

def hamming_distance(x, y):
    dy=len(y)
    dx=len(x) 
    hd=0
    for i in range( dx):
        if dx==dy and x[i] != y[i]:
                hd=hd+1
                
    return(hd)



E=final_binary_key_gen('0', '0', 0.68, 0.3, 1)
    
print(E) 
