#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:54:53 2020

@author: adithya
"""

def reduceToDigit(n):
    Flag = True 
    while(Flag):    
        if n < 10:
            return n 
        else:
            dig = (n%10)
            n = n//10 
            n = n + dig
            
def reduceOneStep(n):
    if n == 0:
        return 0 
    else:
        return 9 if (n % 9 == 0) else (n % 9)
    
print(reduceToDigit(999))
print(reduceOneStep(999))