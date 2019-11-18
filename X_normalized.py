# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:37:01 2019

@author: aleah cute
"""

import numpy as np 

X = np.random.random((5,5))

mean = np.mean(X)
std = np.std(X)
Z = (X - mean)
normalized = Z/std

print(normalized)
