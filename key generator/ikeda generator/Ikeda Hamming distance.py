# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:28:03 2020

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

ax.set_title("Hamming Distance for a Ikeda Based Key Generator after 2 Iteration")

ax.legend()
ax.grid(True)

plt.show()

