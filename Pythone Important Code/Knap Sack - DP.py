#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:02:01 2020

@author: adithya
"""

def KnapSack(n, tweight, weight, val):
    if n == 0 or tweight == 0:
        result = 0
    
    elif tweight < weight[n-1]:
        result = KnapSack(n-1, tweight, weight, val)
        
    else:
        temp1 = KnapSack(n-1, tweight, weight, val)
        temp2 = val[n-1] + KnapSack(n-1, tweight-weight[n-1], weight, val) 
        result = max(temp1, temp2)
        
    return result
        
def KnapSackDp(n, tweight, weight, val, list1):
    if list1[n][tweight] != None:
        return list1[n][tweight]
    
    if n == 0 or tweight == 0:
        result = 0
        
    elif tweight < weight[n-1]:
        result = KnapSackDp(n-1, tweight, weight, val, list1)
        
    else:
        temp1 = KnapSackDp(n-1, tweight, weight, val, list1)
        temp2 = val[n-1] + KnapSackDp(n-1, tweight-weight[n-1], weight, val, list1) 
        result = max(temp1, temp2)
        
    list1[n][tweight] = result 
    return result 

weight = [1,2,4,2,5]
val = [5,3,5,3,2]
tweight = 10 
n = len(weight)

x,y = n,tweight
list1 = [[None for i in range(y+1)] for j in range(x+1)]

print(KnapSack(n, tweight, weight, val))
print(KnapSackDp(n, tweight, weight, val, list1))

