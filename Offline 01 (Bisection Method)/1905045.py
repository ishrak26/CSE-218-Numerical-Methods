# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:17:20 2021

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# f(x) = x^3 - 0.18x^2 + 0.0004752
def f(x):
    return x**3 - 0.18*x**2 + 4.752E-4


# only find the solution    
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
        if err < eps:
            return mid
        
        prev_mid = mid;
    return prev_mid
        

# show error table
def bisection_table(lo, hi, iterations):
    prev_mid = -1
    rows = {'Iteration':[], 'Absolute Relative Approx. Error':[]}
    for i in range(iterations):
        rows['Iteration'].append(i+1)
        
        mid = (lo + hi) / 2
        
        if f(lo) * f(mid) < 0:
            # root lies between lo and mid
            hi = mid
        elif f(mid) * f(hi) < 0:
            # root lies between mid and hi
            lo = mid
        
        if i == 0:
            prev_mid = mid
            rows['Absolute Relative Approx. Error'].append('N/A')
            continue
        
        err = abs((mid - prev_mid) / mid) * 100
        rows['Absolute Relative Approx. Error'].append(err)
        prev_mid = mid;
    
    pd.set_option("display.precision", 20)
    df = pd.DataFrame(rows)
    print(df)
    
    
# plot the graph of f(x) using matplotlib
def plot_curve():
    x = np.arange(0, 0.12, 0.005)
    y = f(x) 

    plt.plot(x, y)
    
    plt.xlabel('x from 0 to 0.12')
    plt.ylabel('y = x^3 - 0.18x^2 + 0.0004752')
    plt.title('Plot of f(x) = x^3 - 0.18x^2 + 0.0004752')
    
    plt.show()
    
    
if __name__ == '__main__':
    """
    Task 1
    """
    print('A graph of the function f(x) = x^3 - 0.18x^2 + 0.0004752 is plotted below:')
    plot_curve()
    print()
    
    print('From the curve, it can be seen that f(x) changes its value from positive to negative between 0 and 0.12')
    print('Approximate location of the root can be visually estimated as 0.06 m')
    print()
    
    """
    Task 2
    """
    print('Bisection method is applied to find the root...')
    print('Approximate value of the root is: ', bisection(0, 0.12, 0.5, 20), 'm')
    print()
    
    """
    Task 3
    """
    print('A table showing the absolute relative approx. error after each iteration of the bisection method for up to 20 iterations:')
    print()
    bisection_table(0, 0.12, 20)
