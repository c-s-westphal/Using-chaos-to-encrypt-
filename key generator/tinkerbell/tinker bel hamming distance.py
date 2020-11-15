# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:32:43 2020

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
 
def x0_generator (d):
    n=len(d)
    d=binary_converter(d)
    d=d/(2**n)
    x0=d*1.5
    
    
    return x0

def y0_generator (U):
    n=len(U)
    U=binary_converter(U)
    U=U/(2**n)
    y0=U*0.9
    y0=y0+0.5
    
    return y0

def tinkerbell_point_generator (x0, y0, N):
    N=int(N)
    x=round(x0,15)
    y=round(y0,15)
    a=0.9
    b=-0.6013
    c=2
    d=0.5
    for i in range (N-1):
        x=x**2-y**2+a*x+b*y
        y=2*x*y+c*x+d*y
    
    return x
                   

def key_value_generator (U, d, N):
    x0=x0_generator(U)
    y0=y0_generator(d)
    (E)=tinkerbell_point_generator(x0, y0, N)
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

N=100
fig, ax = plt.subplots()
output_zeros=np.zeros(5)
for i in range(0,len(five_bits)):
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

ax.set_title("Hamming Distance for a Tinkerbell Based Key Generator after 2 Iterations")

ax.legend()
ax.grid(True)

plt.show()

