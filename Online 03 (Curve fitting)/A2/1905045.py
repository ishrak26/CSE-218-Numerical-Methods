# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:55:16 2022

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np
import matplotlib.pyplot as plt

def partial_pivot(A, B, col, row):
    # find index of the max element staring from row in col
    idx = row
    for i in range(row+1, A.shape[0]):
        if abs(A[i][col]) > abs(A[idx][col]):
            idx = i
    # swap
    A[[row, idx]] = A[[idx, row]]
    B[[row, idx]] = B[[idx, row]]
    
def forward_elimination(A, B):
    for i in range(A.shape[1]):
        # i-th row is the initial pivot row
        partial_pivot(A, B, i, i)
        # i-th row is the pivot row, after possible swapping
        for j in range(i+1, A.shape[0]):
            if A[j][i] != 0:
                fac = A[j][i] / A[i][i]
                A[j] = A[j] - fac * A[i]
                B[j] = B[j] - fac * B[i]

def back_substitution(A, B):
    x = np.empty(A.shape[0])
    for i in range(A.shape[0]-1, -1, -1):
        sum = 0
        for j in range(i+1, A.shape[0]):
            sum = sum + A[i][j] * x[j]
        x[i] = (B[i] - sum) / A[i][i]
    return x

# returns solution matrix
# A is coefficient matrix, B is constant matrix 
def GaussianElimination(A, B):
    forward_elimination(A, B)
    x = back_substitution(A, B)
    return x

def polynomial_regression(x, y, order):
    m = order
    
    sum_x = np.empty(2*m+1)
    sum_y = np.empty(m+1)
    sum_x[0] = x.size
    sum_y[0] = np.sum(y)
    for i in range(1, 2*m+1):
        sum_x[i] = np.sum(np.power(x, i))
    for i in range(1, m+1):
        sum_y[i] = np.sum(y * np.power(x, i))
    
    A = np.empty((m+1, m+1)) # coefficient matrix
    B = np.empty(m+1) # constant matrix
    for i in range(m+1):
        for j in range(m+1):
            A[i][j] = sum_x[i+j]
        B[i] = sum_y[i]
    
    a = GaussianElimination(A, B)
    return a

def polynomial_func(x, a):
    sum = 0.0
    for i in range(a.size):
        sum += a[i] * np.power(x, i)
    return sum

if __name__=='__main__':
    x = np.array(list(i-1900 for i in range(1900, 2001, 10)), float)
    y = np.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])
    plt.scatter(x, y, color='blue')
    plt.title("Plot of No. of Foreign-born Immigrants vs Time")
    plt.xlabel("Time since 1900 (in years)")
    plt.ylabel("No. of Foreign-born Immigrants (in millions)")
    plt.show()
    
    # 3rd order polynomial
    # y = a_0 + a_1 * x + a_2 * x^2 + a_3 * x^3
    print("From the graph, it can be observed that the plot has two bends.")
    print("This plot can be best-fit modelled ny a third-order polynomial equation")
    print("y = a_0 + a_1 * x + a_2 * x^2 + a_3 * x^3")
    print()
    
    order = 3
    a = polynomial_regression(x, y, order)
    print("Unknown cofficients are:")
    for i in range(a.size):
        print(f"\ta_{i} = {a[i]}")
    print("Therefore, equation of the best-fit model is")
    print(f"y = {a[0]} + {a[1]} * x + {a[2]} * x^2 + {a[3]} * x^3 _____ (i)")
    print()
    
    X = np.array(list(i-1900 for i in range(1890, 2011, 1)), float)
    Y = np.empty(X.shape)
    for i in range(X.size):
        Y[i] = polynomial_func(X[i], a)
    plt.scatter(x, y, color='blue')
    plt.plot(X, Y, color='red')
    plt.title("Best-fit Curve Modelling for No. of Foreign-born Immigrants vs Time")
    plt.xlabel("Time since 1900 (in years)")
    plt.ylabel("No. of Foreign-born Immigrants (in millions)")
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.show()
    
    year = 2010
    immigrants = polynomial_func(year-1900, a)
    immigrants_converted = int(round(immigrants, 6) * 1E6)
    print()
    print(f"Using equaion (i), the number of foreign-born immigrants predicted in 2010 is {immigrants} millions", end=' ')
    print(f"or {immigrants_converted:,} (rounded up to nearest integer)")
