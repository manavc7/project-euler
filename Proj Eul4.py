#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:26:35 2023

@author: manavchakravarthy
"""


max_num = 0
num = 0
for i in range(100,1000):
    for k in range(100,1000):
        temp_num = k*i
        temp_reverse = str(temp_num)
        temp_reverse = temp_reverse[::-1]
        if temp_reverse == str(temp_num):       
            if int(temp_reverse)>num:        
                num = temp_num
                reverse = str(num)
                reverse = reverse[::-1]
                if reverse == str(num):
                    max_num = num
                    
print(max_num)