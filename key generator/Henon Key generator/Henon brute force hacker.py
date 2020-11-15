# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:52:12 2020

@author: Charlie
"""

import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import random

 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x0_generator (U):
    n=len(U)
    U=binary_converter(U)
    #U=U/(2**n)
    #to make this 9 bits we make there 511 possibilities for x0 in desired range
    #U=U*511
    #U=int(U)
    U=U/4095
    x0=U*0.5
    x0=x0+1
    
    return x0

def a_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    d=d*4095
    d=int(d)
    d=d/4095
    a=d*0.97
    a=a+0.4
    
    return a

def henon_point_generator (x, y, a, b, N):
    N=int(N)
    for i in range(N-1):
        x=1-(a*x*x)+y
        y=b*x
    
    return x

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    a=a_generator(d)
    y0=0.68
    b=0.3
    (E)=henon_point_generator(x0, y0, a, b, N)
    
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

def henon_hacker (Ep, d, N):
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
                                 
    return Estor

print(final_binary_key_gen('0010', '00111', 100))
print(henon_hacker('0001', '00111', 100))
#print(x0_generator('0010'))



