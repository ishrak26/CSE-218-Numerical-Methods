# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:16:34 2022

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

def find_sum(x, deg):
    sum = 0
    for i in range(0, x.size):
        sum += pow(x[i], deg)
    return sum
        
def find_sum_product(x, y):
    sum = 0
    for i in range(0, x.size):
        sum += x[i]*y[i]
    return sum

# returns (a_0, a_1) of linear model
def linear(x, y):
    n = x.size
    sum_x = find_sum(x, 1)
    sum_y = find_sum(y, 1)
    sum_xy = find_sum_product(x, y)
    sum_x_sq = find_sum(x, 2)
    a_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x * sum_x)
    a_0 = (sum_y - a_1 * sum_x) / n
    return a_0, a_1

# returns (a, b) of exponential model
def exponential(x, y):
    # transform to linear model
    z = np.log(y)
    a_0, a_1 = linear(x, z)
    a = np.exp(a_0)
    b = a_1
    return a, b

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
    