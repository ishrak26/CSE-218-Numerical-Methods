# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:48:54 2022

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    C = 5E-4
    return (6.73*x + 6.725E-8 + 7.26E-4*C) / (3.62E-12 * x + 3.908E-8 * x * C)

# Trapezoidal Rule for n equally spaced sub-intervals
def trapezoid(n, a, b):
    h = (b-a)/n
    sum = 0
    for i in range(1, n):
        sum += f(a + i*h)
    sum *= 2
    sum += f(a) + f(b)
    return sum * h/2

# Simpson's 1/3rd Rule for 2n equally spaced sub-intervals
def simpson(n, a, b):
    n *= 2
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
        y[i] = -simpson(5, x_0, x[i])
    
    plt.plot(x, y, marker='o')
    plt.grid()
    plt.xlabel('Concentration of oxygen, x (mol/cm^3)')
    plt.ylabel('Time, T (seconds)')
    plt.title('Plot of Time vs Concentration of Oxygen')
    plt.show()

if __name__=='__main__':
    x_0 = 1.22E-4
    n = int(input("Enter the value of n: ").strip())
    print()
    
    T = -trapezoid(n, x_0, x_0/2)
    print(f'For {n} equally spaced sub-intervals, Trapezoidal Rule results in T = {T} seconds')
    print()
    print('For n equally spaced sub-intervals from n=1 to n=5, Trapezoidal Rule results:')
    print('n\t\tT (seconds)\t\t\tAbsolute Approx. Relative Error (%)')
    for i in range(60):
        print('-', end='')
    print()
    val = 0
    for i in range(1, 6):
        new_val = -trapezoid(i, x_0, x_0/2)
        if i > 1:
            err = abs((new_val - val) / new_val) * 100
        else:
            err = 'Not Applicable'
        val = new_val
        print(f'{i}\t{val}\t\t\t{err}')
    print()
    
    T = -simpson(n, x_0, x_0/2)
    print(f"For {n*2} equally spaced sub-intervals, Simpson's 1/3rd Rule results in T = {T} seconds")
    print()
    print("For 2n equally spaced sub-intervals from n=1 to n=5, Simpson's 1/3rd Rule results:")
    print('n\t\tT (seconds)\t\t\tAbsolute Approx. Relative Error (%)')
    for i in range(60):
        print('-', end='')
    print()
    val = 0
    for i in range(1, 6):
        new_val = -simpson(i, x_0, x_0/2)
        if i > 1:
            err = abs((new_val - val) / new_val) * 100
        else:
            err = 'Not Applicable'
        val = new_val
        print(f'{i}\t{val}\t\t\t{err}')
    print()
    
    plot_curve(x_0)
