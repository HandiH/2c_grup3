# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:58:57 2019

@author: ASUS
"""

from matplotlib import pyplot as plt

print(1174077%3+2)

def sebaran():
    x = [9,10,11,12,13,14,15]
    y = [21,22,25,31,67,56,30]

    x1 = [4,7,9,3,6]
    y1 = [15,17,19,11,13]

    plt.subplot(221)
    plt.scatter(x,y)
    plt.subplot(222)
    plt.scatter(x1,y1)
    plt.show() 