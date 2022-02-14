# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:10:21 2022

@author: Md. Ishrak Ahsan
"""

import numpy as np

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
# transform to linear model
def exponential(x, y):
    z = np.log(y)
    a_0, a_1 = linear(x, z)
    a = np.exp(a_0)
    b = a_1
    return a, b