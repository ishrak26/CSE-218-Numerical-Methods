# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 07:41:13 2022

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

# find k nearest points
def find_nearest_points(arr, T, k):
    fi = -1
    se = -1
    for i in range(arr.shape[0]):
        if T<arr[i][0]:
            fi = i-1
            se = i
            #print(f'fi {fi} and se {se}')
            while k>0:
                if fi < 0:
                    se = se + k
                    break
                if se >= arr.shape[0]:
                    fi = fi - k
                    break
                if (T-arr[fi][0] < arr[se][0]-T):
                    fi = fi-1
                else:
                    se = se+1
                k = k-1
            return arr[fi+1:se]

def calc_square_bracketed(x):
    sq = np.zeros((x.shape[0], x.shape[0]))
    for i in range(sq.shape[0]):
        sq[i][i] = x[i][1]
    #print(sq)
    for dif in range(1, sq.shape[0]):
        i = 0
        while i+dif < sq.shape[0]:
            sq[i+dif][i] = (sq[i+dif][i+1] - sq[i+dif-1][i]) / (x[i+dif][0] - x[i][0])
            i = i+1
    #print(sq)
    return sq

def calc_f(x, sq, T):
    sum = 0.0
    for i in range(sq.shape[0]):
        # b[k] = sq[k][0]
        pro = sq[i][0]
        for j in range(i):
            pro = pro * (T - x[j][0])
        sum  = sum + pro
    return sum

def Newton_div_diff(order, points, T):
    points = find_nearest_points(points, T, order+1)
    #print(x)
    sq = calc_square_bracketed(points)
    val = calc_f(points, sq, T)
    return val

def Lagrange(order, points, T):
    x = find_nearest_points(points, T, order+1)
    sum = 0.0
    for i in range(order+1):
        # calc L_i
        pro = 1.0
        for j in range(order+1):
            if i != j:
                pro = pro * ((T-x[j][0])/(x[i][0]-x[j][0]))
        pro  = pro * x[i][1]
        sum  = sum + pro
    return sum

# ctrl-4, ctrl-5 = comment, uncomment

if __name__=='__main__':
    # take file input
    f = open('gene.txt', 'r')
    arr = []
    for line in f:
        point = line.strip().split()
        point[0] = float(point[0])
        point[1] = float(point[1])
        arr.append(point)
    f.close()
    points = np.array(arr)
    T = float(input('Enter the value of T: ').strip())
    ans_3 = Newton_div_diff(3, points, T)
    print(ans_3)
    ans_2 = Newton_div_diff(2, points, T)
    err = abs((ans_3-ans_2)/ans_3) * 100
    print(err)
    
    # draw graph
    x = np.arange(points[0][0], points[points.shape[0]-1][0], 0.5)
    y = np.zeros(x.size)
    for i in range(y.size):
        y[i] = Newton_div_diff(3, points, x[i])
    plt.plot(x, y)
    plt.show()
    
# =============================================================================
#     ans_L = Lagrange(3, points, T)
#     print(ans_L)
# =============================================================================
    