# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:23:52 2020

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
    #create hacker thats discrete, this has 1000 possible imputs so roughly 10bits
    x0=d*100
    x0=int(x0)
    x0=x0/100
    x0=x0+1
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*100
    y0=int(y0)
    y0=y0/100
    y0=y0+1
    
    return y0

def rossler_point_generator (x, y, N):
    N=int(N)
    z=27
    a=0.2
    b=0.2
    c=5.7
    dt=0.01
    for i in range (N-1):
        x=x+((-y-z)*dt)
        y=y+((x+a*y)*dt)
        z=z+((b+z*(x-c))*dt)
        
    #discreteise results
    x=abs(x)
    x=x/7.918
    x=x*100
    x=int(x)
    
    return x
                   

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=rossler_point_generator(x0, y0, N)
    
    return E

def final_binary_key_gen (U, d, N):
    E=key_value_generator(U, d, N)
    E=int(E)
    E=bin(E)
    E=E[2:7]
    
    return E

def hamming_distance(x, y):
    dy=len(y)
    dx=len(x) 
    hd=0
    for i in range(2, dx):
        if dx==dy and x[i] != y[i]:
                hd=hd+1
                
    return(hd)

E=final_binary_key_gen('0', '111', 1000)
    
print(E) 

