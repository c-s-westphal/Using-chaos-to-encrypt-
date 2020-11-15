# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:50:47 2020

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
    E=abs(E)/20
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

N=2
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

ax.set_title("Hamming Distance for a Logistic Based Key Generator after 2 Iterations")

ax.legend()
ax.grid(True)

plt.show()

