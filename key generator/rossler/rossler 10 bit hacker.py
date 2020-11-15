# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:55:45 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import random

 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x0_generator (U):
    n=len(U)
    U=binary_converter(U)
    #U=U/(2**n)
    #create hacker thats discrete, this has 1000 possible imputs so roughly 10bits
    #x0=U*4095
    #x0=int(x0)
    x0=U/409.5
    x0=x0+1
    
    return x0

def y0_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    y0=d*4095
    y0=int(y0)
    y0=y0/409.5
    y0=y0+1
    
    return y0

def rossler_point_generator (x0, y0, N):
    N=int(N)
    x=round(x0,12)
    y=round(y0,12)
    z=27
    a=0.2
    b=0.2
    c=5.7
    dt=0.01
    for i in range (N):
        x=x+((-y-z)*dt)
        y=y+((x+a*y)*dt)
        z=z+((b+z*(x-c))*dt)
    
    #x=abs(x)
    #x=x/7.918
    #x=x*10
    #x=int(x)
    
    #discreteise results
    return x
              
def rossler_string_generator (x0, y0, N):
    N=int(N)
    x=np.empty(N+1)
    y=np.empty(N+1)
    z=np.empty(N+1)
    x[0]=round(x0,12)
    y[0]=round(y0,12)
    z[0]=27
    a=0.2
    b=0.2
    c=5.7
    dt=0.01
    for i in range (N):
        x[i+1]=x[i]+((-y[i]-z[i])*dt)
        y[i+1]=y[i]+((x[i]+a*y[i])*dt)
        z[i+1]=z[i]+((b+z[i]*(x[i]-c))*dt)
     
    return x     

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=rossler_point_generator(x0, y0, N)
    
    return E

def final_binary_key_gen (U, d, N):
    v_raw=key_value_generator(U, d, N)
    v_int=abs(int(v_raw))
    v_bin=bin(v_int)
    n=len(v_bin)
    division_factor=2**n
    E=(v_raw/division_factor)*(2**9)
    E=abs(int(E))
    E=bin(E)
    E=E[2:]
    E=E.zfill(12)
    
    return E


def ros_hacker (Ep, d, N):
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

print(final_binary_key_gen('10101', '1000', 100))
print(ros_hacker('0000', '1000', 100))
                    
            




