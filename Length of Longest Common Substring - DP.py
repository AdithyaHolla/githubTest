#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 20:03:01 2020

@author: adithya
"""


def LCS(P, Q, n, m):
    if n == 0 or m == 0 :
        result = 0 
    
    elif P[n-1] == Q[m-1]:
        result = 1 + LCS(P, Q, n-1, m-1)
    
    elif P[n-1] != Q[m-1]:
        temp1 = LCS(P, Q, n-1, m)
        temp2 = LCS(P, Q, n, m-1)
        result = max(temp1, temp2)
        
    return result 

def LCS_DP(P, Q, n, m, arr): 
    if arr[n][m] != None:
        return arr[n][m]
    
    if n == 0 or m == 0 :
        result = 0 
    
    elif P[n-1] == Q[m-1]:
        result = 1 + LCS_DP(P, Q, n-1, m-1, arr)
    
    elif P[n-1] != Q[m-1]:
        temp1 = LCS_DP(P, Q, n-1, m, arr)
        temp2 = LCS_DP(P, Q, n, m-1, arr)
        result = max(temp1, temp2)
    
    arr[n][m] = result 
    return result 

P = "AAABBCXCC"
Q = "ABBCCC"
n = len(P) 
m = len(Q) 
arr = [[None for i in range(m+1)] for j in range(n+1)]
print(LCS(P, Q, n, m))
print(LCS_DP(P, Q, n, m, arr))
