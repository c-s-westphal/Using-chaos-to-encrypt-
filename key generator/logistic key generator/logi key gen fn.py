# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:08:11 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt

''' so we are gonna get 2 strings of binary digits, and
combine them into a new string of binary digits using a 
logistic function. 

 there are 2 parameters that effect a logistic function, 
 r and x. r ranges from 3.6 to 4 and x ranges from 0 to 1.'''
 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def r_generator (d):
    d=binary_converter(d)
    r=((d+10)/(d+9))*3.6
    
    return r

def x_generator (U):
    n=len(U)
    U=binary_converter(U)
    x=(U+0.0001)/(2**n)
    
    return x

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
    E=key_value_generator(U, d, N)
    E=E*(10**7)
    E=int(E)
    E=bin(E)
    
    return E

E=final_binary_key_gen('110', '110', 1000)
    
print(E)  

