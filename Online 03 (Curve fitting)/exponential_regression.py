# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:24:12 2022

@author: Md. Ishrak Ahsan
"""

import numpy as np
import matplotlib.pyplot as plt

# f(b)
def exp_func(b, x, y):
    f = np.sum(x * y * np.exp(b * x)) * np.sum(np.exp(2 * b * x))
    f -= np.sum(y * np.exp(b * x)) * np.sum(x * np.exp(2 * b * x))
    return f

# find the solution of f(b)=0 using bisection method between lo and hi    
def bisection(lo, hi, x, y, max_iterations=25):
    prev_mid = -1.0
    for i in range(max_iterations):
        mid = (lo + hi) / 2
        mid_func = exp_func(mid, x, y)
        if exp_func(lo, x, y) * mid_func < 0:
            # root lies between lo and mid
            hi = mid
        elif mid_func * exp_func(hi, x, y) < 0:
            # root lies between mid and hi
            lo = mid
        if i == 0:
            prev_mid = mid
            continue
        prev_mid = mid;
    return prev_mid

# returns (a, b) of exponential model
# no transformation
def exponential(x, y):
    # find range for bisection of b
    lo = 20
    hi = 25
    b = np.arange(lo, hi, 0.1)
    f = np.empty(b.shape)
    for i in range(f.size):
        f[i] = exp_func(b[i], x, y)
    print(b)
    print(f)
    plt.axhline()
    plt.plot(b, f, color='red')
    plt.show()
    
    b = bisection(lo, hi, x, y)
    a = np.sum(y * np.exp(b * x)) / np.sum(np.exp(2 * b * x))
    return a, b
    
    
if __name__=='__main__':
    arr = list(i/100 for i in range(1, 22, 2))
    arr.insert(0, 0)
    x = np.array(arr)
    y = np.array([1, 1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78])
# =============================================================================
#     x = np.array([0, 1, 3, 5, 7, 9], dtype=float)
#     y = np.array([1, 0.891, 0.708, 0.562, 0.447, 0.355], dtype=float)
# =============================================================================
    a, b = exponential(x, y)
    Y = a * np.exp(b * x)
    plt.plot(x, y, color='green')
    plt.plot(x, Y, color='red')
    plt.show()
    