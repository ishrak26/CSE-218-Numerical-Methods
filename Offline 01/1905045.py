# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:17:20 2021

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 0.18*x**2 + 4.752E-4
    

def bisection(lo, hi, epsilon, rem_iterations):
    if rem_iterations == 0:
        return lo
    if lo > hi:
        (lo, hi) = (hi, lo)
    mid = (lo + hi) / 2;
    
    if f(lo) * f(mid) < 0:
        # root lies between lo and mid
        return bisection(lo, mid, epsilon, rem_iterations - 1)
    elif f(mid) * f(hi) < 0:
        # root lies between mid and hi
        return bisection(mid, hi, epsilon, rem_iterations - 1)
    return mid
    

def plot_curve():
    x = np.arange(0, 0.12, 0.005)
    y = f(x) 

    plt.plot(x, y)
    plt.show()
    

if __name__ == '__main__':
    plot_curve()
    print(bisection(0, 0.12, 0.5, 20))

