#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:24:34 2020

@author: adithya
"""
class Deque:
    
    def __init__(self):
        self.item=[]
        
    def add_f(self, data):
        self.item.insert(0, data)
        
    def add_b(self, data):
        self.item.append(data)
    
    def remove_f(self):
        if self.item:
            return self.item.pop(0)
        else:
            return None 
        
    def remove_b(self):
        if self.item:
            return self.item.pop()
        else: 
            return None
        
    def peek_f(self):
        if self.item:
            return self.item[0]
        else: 
            return None
    
    def peek_b(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    
    def is_empty(self):
        return self.item == []
        
    def size(self):
        return len(self.item)
    
class Check_Palindrome(Deque):
    
    def __init__(self):
        super().__init__()
    
    def check(self):
        
        if len(self.item)%2 == 0:
            for i in range(len(self.item)//2):
                if self.remove_b() == self.remove_f():
                    continue
                else:
                    return f"Not a palindrome"
                    
            if not self.item:
                return f"Is a palindrome"
        
        else:
            for i in range(len(self.item)//2):
                if self.remove_b() == self.remove_f():
                    continue
                else:
                    return f"Not a palindrome"
            
            if len(self.item) == 1:
                return f"Is a palindrome"
            
            else:
                return f"Empty String"
            
        
        
def main():
    x = input("Input the Palindrome: ")
    d = Check_Palindrome()
    for l in x:
        d.add_f(l)
    print(d.check())
    
    
if __name__=="__main__":main()        
        
    