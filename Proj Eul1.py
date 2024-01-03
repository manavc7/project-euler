#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:04:19 2023

@author: manavchakravarthy
"""
total_sum = 0

for number in range(1000):
    # Check if the number is a multiple of 3 or 5
    if number % 3 == 0 or number % 5 == 0:
        # Add the number to the sum
        total_sum += number

# Print the result
print("The sum of all multiples of 3 or 5 below 1000 is:", total_sum)