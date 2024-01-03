#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:40:00 2023

@author: manavchakravarthy
"""

sum_squares = [0] * 100
first_100 = [0] * 100

for i in range(0,100):
    sum_squares[i]=(i+1)**2
    first_100[i] = i+1
    
print(sum(first_100))
print(sum(sum_squares))
print((((sum(first_100))**2) - sum(sum_squares)))
