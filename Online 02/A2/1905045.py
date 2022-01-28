# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:15:57 2022

@author: Md. Ishrak Ahsan
"""

import csv
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

if __name__=='__main__':
    arr1 = []
    arr2 = []
    with open('dissolveO2.csv', 'r') as file:
        csv_dict = csv.DictReader(file)
        for row in csv_dict:
            #row = dict(row)
            lis1 = []
            lis2 = []
            lis1.append(float(row['temparature']))
            lis2.append(float(row['temparature']))
            lis1.append(float(row['solubility_1']))
            lis2.append(float(row['solubility_2']))
            arr1.append(lis1)
            arr2.append(lis2)
    points1 = np.array(arr1)
    points2 = np.array(arr2)
    T = float(input('Enter the value of T: ').strip())
    ans1 = Newton_div_diff(4, points1, T)
    ans2 = Newton_div_diff(4, points2, T)
    print('For 1 bar pressure, dissolved O2 is ', ans1, 'mg/L')
    print('For 2 bar pressure, dissolved O2 is ', ans2, 'mg/L')
    ans3 = Newton_div_diff(3, points1, T)
    ans4 = Newton_div_diff(3, points2, T)
    err1 = abs((ans1-ans3)/ans1)*100
    err2 = abs((ans2-ans4)/ans2)*100
    print('For 1 bar pressure, error is ', err1, '%')
    print('For 2 bar pressure, error is ', err2, '%')
    
    # draw graph
    x = np.arange(points1[0][0], points1[points1.shape[0]-1][0], 0.5)
    y1 = np.zeros(x.size)
    y2 = np.zeros(x.size)
    for i in range(y1.size):
        y1[i] = Newton_div_diff(4, points1, x[i])
        y2[i] = Newton_div_diff(4, points2, x[i])
    
    plt.plot(x, y1, label='1 bar')
    plt.plot(x, y2, label='2 bar')
    plt.title('Plot of Dissolved O2 vs Temperature')
    plt.xlabel('Temperature in Celsius')
    plt.ylabel('Dissolved O2')
    plt.legend()
    plt.show()
    