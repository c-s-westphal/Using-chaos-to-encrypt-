# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:33:36 2020

@author: Charlie
"""
import statistics as stat
import scipy.stats as sci
import matplotlib.pyplot as plt
import scipy
import itertools as itr
import math
import numpy as np

__all__ = ['perm_from_int', 'int_from_perm', 'int_from_code', 'code_from_int',
           'perm_from_code', 'code_from_perm', 'iter_perm']


def _perm_from_int_pick(base, num):
    """
    :type base: list
    :type num: int
    :rtype: list
    """
    pass

def _perm_from_code_pick(base, code):
    """
    :type base: list
    :type code: list
    :rtype: list
    """
    pass

def _code_from_perm_pick(base, perm):
    """
    :type base: list
    :type perm: list
    :rtype: list
    """
    pass

def _int_from_perm_pick(base, perm):
    """
    :type base: list
    :type perm: list
    :rtype: int
    """
    pass

def _int_from_code_pick(code):
    """
    :type code: list
    :rtype: int
    """
    pass

def iter_perm(base, *rargs, pick=None):
    """
    :type base: list
    :param rargs: range args [start,] stop[, step]
    :rtype: generator
    """
    if not rargs:
        rargs = [math.factorial(len(base))]
    for i in range(*rargs):
        yield perm_from_int(base, i, pick=pick)

def int_from_code(code):
    """
    :type code: list
    :rtype: int
    """
    num = 0
    for i, v in enumerate(reversed(code), 1):
        num *= i
        num += v

    return num

def code_from_int(size, num):
    """
    :type size: int
    :type num: int
    :rtype: list
    """
    code = []
    for i in range(size):
        num, j = divmod(num, size - i)
        code.append(j)

    return code


def perm_from_code(base, code, pick=None):
    """
    :type base: list
    :type code: list
    :rtype: list
    """
    if pick:
        return _perm_from_code_pick(base, code)

    perm = base.copy()
    for i in range(len(base) - 1):
        j = code[i]
        perm[i], perm[i+j] = perm[i+j], perm[i]

    return perm

def perm_from_int(base, num, pick=None):
    """
    :type base: list
    :type num: int
    :rtype: list
    """
    code = code_from_int(len(base), num)
    return perm_from_code(base, code, pick=pick)

#L4 = [1,2,3,4]
#print(perm_from_int(L4, 15))
    
def circle_product (xi, c, A):
    Xi=perm_from_int(A, xi)
    C=perm_from_int(A, c)
    #output=np.empty(len(A))
    output=[0,0,0,0,0,0]
    for i in range(len(A)):
        output[i]=C[(Xi[i]-1)]
    
    return output

def labeler (A, Xi):
    for i in range(math.factorial(len(A))):
        if perm_from_int(A, i)==Xi:
            return i
        
def rhs (xi, c, A):
    T1=labeler(A, circle_product(xi, c, A))
    T2=labeler(A, list(reversed(circle_product(xi, c, A))))
    
    return abs(T1-T2)

def lambic_function (xi, c, A):
    r=rhs(xi, c, A)
    rl=perm_from_int(A, r)
    fs=circle_product(xi, r, A)
    fv=labeler(A, fs)
    
    return fv

A=[1,2,3,4,5,6]
numsteps=500
fin=np.empty(numsteps+1)
for i in range(numsteps):
    fin[i]=lambic_function(29+i, 1, A)
    
n=range(numsteps+1)
plt.plot(n,fin)

