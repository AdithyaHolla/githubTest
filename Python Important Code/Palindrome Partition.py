#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:34:00 2020

@author: adithya
"""

class Partition:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n 
    
    def split(self):
        self.l = len(self.a)
        self.a1 = self.a[0:self.n]
        self.a2 = self.a[self.n:self.l]
        self.b1 = self.b[0:self.n]
        self.b2 = self.b[self.n:self.l]
        
    def concat(self):
        self.a1 = self.a1 + self.b2
        self.b1 = self.b1 + self.a2
        print("The first string is :" + self.a1, "\nThe second string is :" + self.b1)
        
    def check(self, stg):
        for i in range(self.l//2):
            j = i + 1 
            j = -j
            print(i, j)
            if stg[i] == stg[j]:
                continue
            else:
                return False 
        return True
            
            
p = Partition("nibbba", "abtina ", 2)
p.split()
p.concat()

print(p.check(p.a1))
print(p.check(p.b1))
a = p.check(p.a1) or p.check(p.b1)
print(a)
                
            


