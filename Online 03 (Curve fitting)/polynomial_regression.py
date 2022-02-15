# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:04:53 2022

@author: Md. Ishrak Ahsan
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
    A = np.empty((m+1, m+1))
    B = np.empty(m+1)
    
    sum_x = np.empty(2*m+1)
    sum_y = np.empty(m+1)
    sum_x[0] = x.size
    sum_y[0] = np.sum(y)
    for i in range(1, 2*m+1):
        sum_x[i] = np.sum(np.power(x, i))
    for i in range(1, m+1):
        sum_y[i] = np.sum(y * np.power(x, i))
    
    for i in range(m+1):
        for j in range(m+1):
            A[i][j] = sum_x[i+j]
        B[i] = sum_y[i]
    a = GaussianElimination(A, B)
    return a

def polynomial_f(x, a):
    sum = 0.0
    for i in range(a.size):
        sum += a[i] * np.power(x, i)
    return sum

if __name__=='__main__':
    x = np.array([80, 40, -40, -120, -200, -280, -340], float)
    y = np.array([6.47, 6.24, 5.72, 5.09, 4.3, 3.33, 2.45]) * 1E-6
    # plt.plot(x, y, color='red')
    plt.scatter(x, y, color='red')
    a = polynomial_regression(x, y, 2)
    
    Y = np.empty(x.shape)
    for i in range(x.size):
        Y[i] = polynomial_f(x[i], a)
    # plt.plot(x, Y, color='green')
    
    
    
    