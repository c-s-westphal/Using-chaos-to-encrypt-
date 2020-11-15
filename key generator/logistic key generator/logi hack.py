# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:56:25 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import random

''' so we are gonna get 2 strings of binary digits, and
combine them into a new string of binary digits using a 
logistic function. 

 there are 2 parameters that effect a logistic function, 
 r and x. r ranges from 3.6 to 4 and x ranges from 0 to 1.'''
 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x_generator (U):
    n=len(U)
    U=binary_converter(U)
    x=U/4095
    
    return x
 
def r_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    d=d*4095
    d=int(d)
    d=d/4095
    r=((d+10)/(d+9))*3.6
    
    return r

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

def logi_point_generator (r, x0, N):
    N=int(N)
    point=round(x0,15)
    for i in range (N-1):
        point=round(logistic(point,r),12)
        
    return point

def key_value_generator (U, d, N):
    x=x_generator(U)
    r=r_generator(d)
    E=logi_point_generator(r, x, N)
    
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

def logi_hacker (Ep, d, N):
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

print(final_binary_key_gen('110', '110', 100))
print(logi_hacker('0000', '110', 100))
    
 



