# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:04:34 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

 
def binary_converter (b):
     d=int(b,2)
     
     return d
 
def x0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    x0=U*10
    x0=x0+1
    
    return x0

def y0_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    y0=d*10
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
              
def rossler_string_generator (x0, y0, N):
    N=int(N)
    x=np.empty(N)
    y=np.empty(N)
    z=np.empty(N)
    x[0]=round(x0,15)
    y[0]=round(y0,15)
    z[0]=27
    a=0.2
    b=0.2
    c=5.7
    dt=0.01
    for i in range (N-1):
        x[i+1]=x[i]+((-y[i]-z[i])*dt)
        y[i+1]=y[i]+((x[i]+a*y[i])*dt)
        z[i+1]=z[i]+((b+z[i]*(x[i]-c))*dt)
    
    return x     

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=rossler_point_generator(x0, y0, N)
    E=round(E, 15)
    E=E*(10**15)
    E=abs(E)
    E=int(E)
    
    return E

def final_binary_key_gen (U, d, N):
    E=key_value_generator(U, d, N)
    E=bin(E)
    E=E[2:34]
    
    return E


def ros_hacker (U, Ep, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    E_string=rossler_string_generator(x0, y0, N)
    Utry=np.linspace(1,11,(100))
    #d=binary_converter(d)
    #reverse of Ep
    Ep=binary_converter(Ep)
    Ep=Ep/(10**7)
    N=int(N)
    E=0
    U=np.empty(N)
    for i in range(100):
        for j in range(N):
            E=rossler_point_generator(Utry[i], y0, j)
            if E_string[j]==E:
                if E==Ep:
                    return Utry[i]
            
x=ros_hacker('0','100101110000011000100010101','0','1000')
print(x)




    


    

