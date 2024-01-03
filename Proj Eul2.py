#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:14:30 2023

@author: manavchakravarthy
"""
import numpy as np

total_sum = 0
n = np.zeros(100)
n[1] = 1
n[2] = 2

for i in range(3,100):
    n[i] = n[i-1] + n[i-2]
    
for k in range(100):
    if n[k]%2 == 0 and n[k]<4000000:
        total_sum += n[k] 
    
print("the sum of the even-valued terms of tbe fibonacci sequence below four million is: " + str(total_sum))