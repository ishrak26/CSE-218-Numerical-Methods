# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:45:29 2021

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

PI = 3.14159

# f(h) = pi*h^3 - 12*pi*h^2 + 15
def f(h):
    return PI * (h**3) - 12 * PI * (h**2) + 15


# derivative: f_prime(h) = 3*pi*h^2 - 24*pi*h
def f_prime(h):
    return 3 * PI * (h**2) - 24 * PI * h


# plot the curve in a range from lo to hi
def plot_curve(lo, hi, step):
    x = np.arange(lo, hi, step)
    y = f(x)
    y2 = x*0
    
    plt.plot(x, y)
    plt.plot(x, y2)
    
    plt.xlabel('x from ' + str(lo) + ' to ' + str(hi))
    plt.ylabel('y = f(x)')
    plt.title('Plot of f(h) = pi*h^3 - 12*pi*h^2 + 15')
    
    plt.show()


# solve for f(x)=0 using Newton-Raphson method    
def solve(x, eps):
    table = {'Iteration':[], 'Root Estimate':[], 'Error':[]}
    new_x = -1
    max_iteration = 20
    for i in range(max_iteration):
        table['Iteration'].append(i+1)
        new_x = x - (f(x) / f_prime(x))
        table['Root Estimate'].append(new_x)
        err = abs((new_x - x) / new_x) * 100
        table['Error'].append(err)
        x = new_x
        if (err <= eps):
            break
    pd.set_option("display.precision", 20)
    df = pd.DataFrame(table)
    print(df)
    return x

  
if __name__ == '__main__':
    print('The value of h must lie between 0 and 8')
    plot_curve(0, 8, 0.005)
    print('From the graph, it can be seen that root exists very close to 0')
    print('The plot is now zoomed in')
    plot_curve(0, 1, 0.005)
    print('Initial guess from the graph is h=0.6 ft')
    initial_guess = 0.6
    root = solve(initial_guess, 0.05)
    print('Required value of h is h =', root, 'ft')
 
    