#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:37:43 2023

@author: manavchakravarthy
"""

def largest_prime_factor(num):
    i = 2    
    while i * i <= num:
        if num%i != 0 :
            i += 1
        else: 
            num //= i
    return num

number_to_factorise = 600851475143
largest_prime_factor(number_to_factorise)
print(largest_prime_factor(number_to_factorise))
            
     