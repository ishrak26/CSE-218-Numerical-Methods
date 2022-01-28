# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:48:54 2022

@author: Md. Ishrak Ahsan
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    C = 5E-4
    return (6.73*x + 6.725E-8 + 7.26E-4*C) / (3.62E-12 * x + 3.908E-8 * x * C)

def trapezoid(n, a, b):
    h = (b-a)/n
    sum = 0
    for i in range(1, n):
        sum += f(a + i*h)
    sum *= 2
    sum += f(a) + f(b)
    return sum * h/2

def simpson(n, a, b):
    h = (b-a)/n
    sum = f(a) + f(b)
    for i in range(1, n):
        if i%2==0:
            sum += 2*f(a+i*h)
        else:
            sum += 4*f(a+i*h)
    return sum*h/3

def plot_curve(x_0):
    x = np.array([1.22, 1.20, 1.0, 0.8, 0.6, 0.4, 0.2])
    x *= 1E-4
    y = np.empty(x.shape)
    for i in range(x.size):
        y[i] = -simpson(10, x_0, x[i])
    
    plt.plot(x, y, marker='o')
    plt.show()

if __name__=='__main__':
    x_0 = 1.22E-4
    n = int(input("Enter the number of sub-intervals: ").strip())
    T = -trapezoid(n, x_0, x_0/2)
    print(T)
    print('Trapezoid:')
    val = 0
    for i in range(1, 6):
        new_val = -trapezoid(i, x_0, x_0/2)
        if i > 1:
            err = abs((new_val - val) / new_val) * 100
            print(i, new_val, err)
        else:
            print(i, new_val, 'N/A')
        val = new_val
    
    print()
    T = -simpson(2*n, x_0, x_0/2)
    print(T)
    print('Simpsons:')
    val = 0
    for i in range(1, 6):
        new_val = -simpson(i*2, x_0, x_0/2)
        if i > 1:
            err = abs((new_val - val) / new_val) * 100
            print(i, new_val, err)
        else:
            print(i, new_val, 'N/A')
        val = new_val 
    
    plot_curve(x_0)
    
    