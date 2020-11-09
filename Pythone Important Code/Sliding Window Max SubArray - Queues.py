#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:57:26 2020

@author: adithya
"""

class Queue():
    def __init__(self):
        self.arr = []
        
    def addf(self, data):
        self.arr.insert(0, data)
    
    def addb(self, data):
        self.arr.append(data)
    
    def removef(self):
        if self.arr:
            self.arr.pop(0)
        
    def removeb(self):
        if self.arr:
            self.arr.pop()
            
    def is_empty(self):
        if self.arr:
            return False 
        else:
            return True 
        
    def peekf(self):
        if self.arr:
            return self.arr[0]
    
    def peekb(self):
        if self.arr:
            return self.arr[-1]
    
class Check_Max(Queue):
    
    def __init__(self, arr, n, k):
        super().__init__()
        self.arr = arr
        self.n = n 
        self.k = k
        
        
    def check(self):
        
            Q = Queue()
            
            
            for i in range(self.k):
                
                while (not(Q.is_empty()) and (self.arr[i] >= self.arr[Q.peekb()]) ):
                    Q.removeb()
                 
                Q.addb(i)
            
            
            for j in range(self.k, self.n):
                
                print(self.arr[Q.peekf()])
                
                while (not(Q.is_empty()) and ((j-self.k) >= Q.peekf())):
                    Q.removef()
                    
                while (not(Q.is_empty()) and (self.arr[j] >= self.arr[Q.peekb()]) ):
                    Q.removeb()
                
                Q.addb(j)
            
            print(self.arr[Q.peekf()])

def main():
    
    arr = [3, 2, 1, 0, -1, 5, 0, 0, 0, -5, 20]
    n = len(arr)
    k = 3
    S = Check_Max(arr, n, k)
    S.check()
    
if __name__ == "__main__":
    main()
            
            