# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 22:02:22 2022

@author: Md. Ishrak Ahsan (1905045)
"""

import numpy as np

def partial_pivot(A, B, col, row):
    # find index of the max element staring from row in col
    idx = row
    for i in range(row+1, A[row].size):
        if A[i][col] > A[idx][col]:
            idx = i
    # swap
    A[[row, idx]] = A[[idx, row]]
    B[[row, idx]] = B[[idx, row]]
    

def forward_elimination(A, B, pivot, showall):
    for i in range(B.size):
        # i-th row is the initial pivot row
        if pivot:
            partial_pivot(A, B, i, i)
        for j in range(i+1, B.size):
            if A[j][i] != 0:
                fac = A[j][i] / A[i][i]
                A[j] = A[j] - fac * A[i]
                B[j] = B[j] - fac * B[i]
        if showall:
            print(A)
            print(B)


def back_substitution(A, B):
    x = np.empty(B.size)
    for i in range(B.size-1, -1, -1):
        sum = 0
        for j in range(i+1, B.size):
            sum = sum + A[i][j] * x[j]
        x[i] = (B[i] - sum) / A[i][i]
    return x


def GaussianElimination(A, B, pivot=True, showall=True):
    forward_elimination(A, B, pivot, showall)
    x = back_substitution(A, B)
    return x


def take_arr_input(n):
    arr = []
    for i in range(n):
        row = input().strip().split()
        for j in range(len(row)):
            row[j] = float(row[j])
        arr.append(row)  
    return np.array(arr)


if __name__ == '__main__':
    n = int(input())
    A = take_arr_input(n)
    B = take_arr_input(n)
    x = GaussianElimination(A, B)
    print(x)
            
    