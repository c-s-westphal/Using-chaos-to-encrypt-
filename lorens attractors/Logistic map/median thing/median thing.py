# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:38:27 2020

@author: Charlie
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic (x, r):
    xdot=(x*r)-(x*x*r)
    
    return xdot

#dont want to use an array
def median (mid_val, logi_val, rnew):
    for i in range(mid_val):
        logi_val=logistic(logi_val, rnew)
        
    return logi_val
#going to try and define another function which gives the mean of a few meds
    

    
numsteps=999
rs=np.linspace(3.6,4., num=numsteps)
med_logi=np.zeros(numsteps+1)
med_logis=np.zeros(numsteps)
n=range(numsteps)
k=0

for i in range(numsteps):
    med_logi[i]=median(500, 0.1, rs[i])
    #med_logi_smooth[i]=(med_logi[i-1]+med_logi[i]+med_logi[i+1])/3
    
for i in range(numsteps):
  med_logis[i]=median(501,0.1, rs[i])

med_logi_av=np.zeros(numsteps)

for i in range(numsteps):
    med_logi_av[i]=(med_logi[i]+med_logis[i])/2

'''#smooth out
    
med_logi_smooth=np.zeros(numsteps)



for i in range(numsteps-28):
    med_logi_smooth[i]=(med_logi_av[i-28]+med_logi_av[i-27]+med_logi_av[i-26]+med_logi_av[i-25]
                        +med_logi_av[i-24]+med_logi_av[i-23]+med_logi_av[i-22]+med_logi_av[i-21]+
                        med_logi_av[i-20]+med_logi_av[i-19]+med_logi_av[i-18]+med_logi_av[i-17]+
                        med_logi_av[i-16]+med_logi_av[i-15]+med_logi_av[i-14]+med_logi_av[i-13]+
                        med_logi_av[i-12]+med_logi_av[i-11]+med_logi_av[i-10]+med_logi_av[i-9]+
                        med_logi_av[i-8]+med_logi_av[i-7]+med_logi_av[i-6]+med_logi_av[i-5]+med_logi_av[i-4]
                        +med_logi_av[i-3]+med_logi_av[i-2]+med_logi_av[i-1]+med_logi_av[i]+
                        med_logi_av[i+1]+med_logi_av[i+2]+med_logi_av[i+3]+med_logi_av[i+4]+med_logi_av[i+5]+
                        med_logi_av[i+6]+med_logi_av[i+7]+med_logi_av[i+8]+med_logi_av[i+9]+med_logi_av[i+10]+
                        med_logi_av[i+11]+med_logi_av[i+12]+med_logi_av[i+13]+med_logi_av[i+14]+med_logi_av[i+15]
                        +med_logi_av[i+16]+med_logi_av[i+17]+med_logi_av[i+18]+med_logi_av[i+19]+med_logi_av[i+20]
                        +med_logi_av[i+21]+med_logi_av[i+22]+med_logi_av[i+23]+med_logi_av[i+24]+med_logi_av[i+25]+med_logi_av[i+26]+med_logi_av[i+27]+med_logi_av[i+28])/57
    



#for i in range(numsteps-57)'''

plt.plot(rs,med_logi_av)

print(med_logi_av[0])






        




