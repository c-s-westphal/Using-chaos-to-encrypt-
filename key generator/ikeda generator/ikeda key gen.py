# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:13:52 2020

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
    x0=d*9
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*9
    
    return y0

def ikeda_point_generator (x0, y0, N):
    N=int(N)
    x=round(x0,32)
    y=round(y0,32)
    t=0
    u=0.918
    for i in range(N-1):
        t=0.4-(6/(1+x*x+y*y))
        x=1+u*(x*math.cos(math.degrees(t))-y*math.sin(math.degrees(t)))
        y=u*(x*math.sin(math.degrees(t))+y*math.cos(math.degrees(t)))
    
    return x
                   
        
#    return point_y

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=ikeda_point_generator(x0, y0, N)
    E=round(E, 7)
    
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

E=final_binary_key_gen('0111111', '10001001010', 1000)
    
print(E) 

