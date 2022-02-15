# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:16:34 2022

@author: User
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

# returns (a_0, a_1) of linear model
def linear(x, y):
    n = x.size
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x*y)
    sum_x_sq = np.sum(x*x)
    a_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x * sum_x)
    a_0 = (sum_y - a_1 * sum_x) / n
    return a_0, a_1

# returns (a, b) of exponential model
def exponential(x, y):
    # transform to linear model
    z = np.log(y)
    # a_0, a_1 = linear(x, z)
    a_0, a_1 = polynomial_regression(x, z, 1)
    a = np.exp(a_0)
    b = a_1
    return a, b

# =============================================================================
# # f(b)
# def exp_func(b, x, y):
#     f = np.sum(x * y * np.exp(b * x)) * np.sum(np.exp(2 * b * x))
#     f -= np.sum(y * np.exp(b * x)) * np.sum(x * np.exp(2 * b * x))
#     return f
# 
# # find the solution of f(b)=0 using bisection method between lo and hi    
# def bisection(lo, hi, x, y, max_iterations=25):
#     prev_mid = -1.0
#     for i in range(max_iterations):
#         mid = (lo + hi) / 2
#         mid_func = exp_func(mid, x, y)
#         if exp_func(lo, x, y) * mid_func < 0:
#             # root lies between lo and mid
#             hi = mid
#         elif mid_func * exp_func(hi, x, y) < 0:
#             # root lies between mid and hi
#             lo = mid
#         if i == 0:
#             prev_mid = mid
#             continue
#         prev_mid = mid;
#     return prev_mid
# 
# # returns (a, b) of exponential model
# # no transformation
# def exponential(x, y):
#     # find range for bisection of b
#     lo = 0
#     hi = 0.05
#     bs = np.arange(lo, hi, 0.001)
#     f = np.empty(bs.shape)
#     for i in range(f.size):
#         f[i] = exp_func(bs[i], x, y)
#     plt.axhline()
#     plt.plot(bs, f, color='red')
#     plt.show()
#     
#     b = bisection(lo, hi, x, y)
#     a = np.sum(y * np.exp(b * x)) / np.sum(np.exp(2 * b * x))
#     return a, b
# 
# =============================================================================
if __name__=='__main__':
    arr = list(i/100 for i in range(1, 22, 2))
    arr.insert(0, 0)
    x = np.array(arr)
    y = np.array([1, 1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78])
    plt.plot(x, y, color='red')
    
    a, b = exponential(x, y)
    Y = a * np.exp(b * x)
    plt.plot(x, Y, color='blue')
    plt.show()
    ans = a * np.exp(b * 0.16)
    print(round(ans, 2))
    