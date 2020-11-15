# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:23:48 2020

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
    x0=0
    d=binary_converter(d)
    d=d/(2**n)
    x0=d*0.1
    x0=x0+1.4
    x0=-x0
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*0.1
    y0=y0+1.4
    y0=-y0
    
    
    return y0
    
def tinkerbell_point_generator (x0, y0, N):
    N=int(N)
    x=np.empty(N+1)
    y=np.empty(N+1)
    x[0]=round(x0,32)
    y[0]=round(y0,32)
    a=0.9
    b=-0.6013
    c=2
    d=0.5
    for i in range (N):
        x[i+1]=x[i]**2-y[i]**2+a*x[i]+b*y[i]
        y[i+1]=2*x[i]*y[i]+c*x[i]+d*y[i]
    
    return abs(x[N])
                   

def key_value_generator (U, d, N):
    x0=x0_generator(d)
    y0=y0_generator(U)
    E=tinkerbell_point_generator(x0, y0, N)
    E=abs(round(E, 32))
    
    return E

def final_binary_key_gen (U, d, N):
    E=key_value_generator(U, d, N)
    E=abs(E)/1.5
    E=E*(2**32)
    E=int(E)
    E=bin(E)
    E=E[2:]
    E=E.zfill(32)
    
    return E

def hamming_distance(x, y):
    dy=len(y)
    dx=len(x) 
    hd=0
    for i in range( dx):
        if dx==dy and x[i] != y[i]:
                hd=hd+1
                
    return(hd)

five_bits=['00000', '00001',
'00010',
'00011' ,
'00100' ,
'00101' ,
'00110' ,
'00111' ,
'01000' ,
'01001' ,
'01010' ,
'01011' ,
'01100' ,
'01101' ,
'01110' ,
'01111' ,
'10000' ,
'10001' ,
'10010' ,
'10011' ,
'10100',
'10101' ,
'10110' ,
'10111' ,
'11000' ,
'11001' ,
'11010' ,
'11011' ,
'11100' ,
'11101',
'11110' ,
'11111',]

N=1000
print(key_value_generator('11', '111', N))
fig, ax = plt.subplots()
output_zeros=np.zeros(5)
for i in range(len(five_bits)):
    for j in range(len(five_bits)):
        if i != j:
            hdinput=hamming_distance(five_bits[i], five_bits[j])
            E=final_binary_key_gen('00000', five_bits[i], N)
            E2=final_binary_key_gen('00000', five_bits[j], N)
            hdoutput=hamming_distance(E, E2)
            #print(hdinput, hdoutput)
                
            ax.scatter(hdinput, hdoutput, color='black', alpha=0.1, edgecolors='none')
            
                        

                
                
        
ax.set_xlabel("Hamming Distance Between d1 and d2")
ax.set_ylabel("Hamming Distance Between E1 and E2")

ax.set_title("Hamming Distance for a Tinkerbell Based Key Generator")

ax.legend()
ax.grid(True)

plt.show()

#print(key_value_generator('11', '111', N))