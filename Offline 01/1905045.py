# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:17:20 2021

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**3 - 0.18*x**2 + 4.752E-4

    
def bisection(lo, hi, eps, max_iterations):
    prev_mid = -1
    for i in range(max_iterations):
        mid = (lo + hi) / 2
        
        if f(lo) * f(mid) < 0:
            # root lies between lo and mid
            hi = mid
        elif f(mid) * f(hi) < 0:
            # root lies between mid and hi
            lo = mid
        if i == 0:
            prev_mid = mid
            continue
        err = abs((mid - prev_mid) / mid) * 100
        print(i, err)
        if err < eps:
            return mid
        prev_mid = mid;


def bisection(lo, hi, iterations):
    prev_mid = -1
    rows = {'Iteration':[], 'Absolute Relative Approx. Error':[]}
    for i in range(iterations):
        mid = (lo + hi) / 2
        
        if f(lo) * f(mid) < 0:
            # root lies between lo and mid
            hi = mid
        elif f(mid) * f(hi) < 0:
            # root lies between mid and hi
            lo = mid
        if i == 0:
            prev_mid = mid
            continue
        err = abs((mid - prev_mid) / mid) * 100
        rows['Iteration'].append(i+1)
        rows['Absolute Relative Approx. Error'].append(err)
        prev_mid = mid;
    pd.set_option("display.precision", 20)
    df = pd.DataFrame(rows)
    print(df)
    return prev_mid
    

def plot_curve():
    x = np.arange(0, 0.12, 0.005)
    y = f(x) 

    plt.plot(x, y)
    plt.show()
    

if __name__ == '__main__':
    plot_curve()
    print(bisection, 0, 0.12, 0.5, 20)
    print(bisection(0, 0.12, 20))

