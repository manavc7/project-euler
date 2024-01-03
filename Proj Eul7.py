#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:59:34 2023

@author: manavchakravarthy
"""

def prime_numbers(n):
    primes = []
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

prime_list = prime_numbers(1000000)
print(prime_list)

print(prime_list[10000])