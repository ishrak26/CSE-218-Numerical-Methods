# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:10:21 2022

@author: Md. Ishrak Ahsan
"""

import numpy as np

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
