# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 08:45:15 2019

@author: aleah cute
"""

import numpy as np

A = np.arange(1,101,1)
B = np.reshape(A,(10,10))
C = B * B
D = C%3
E = C[D==0]

print(E)

