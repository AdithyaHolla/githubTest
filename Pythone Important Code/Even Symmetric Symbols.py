#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:35:14 2020

@author: adithya
"""

class Stack():
 
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return None
    
    def peek(self):
        if self.data:
            return self.data[-1]
        else:
            return None 
        
    def size(self):
        return len(self.data)
            
    
    def is_empty(self):
        return self.data == [] 
        
    def check(input_string):
        
        pairs = {"{":"}", "[":"]", "(":")"}
        symbol_f = ["{", "[", "("]
        symbol_b = ["}", "]", ")"]
        
        T = Stack()
        index = 0 
        
        while index < len(input_string):
            st = input_string[index]
            
            if len(input_string)%2 != 0:
                return False 
            if st in symbol_f:
                T.push(st)
            else:
                if st in symbol_b and not T.is_empty():
                    if st == pairs[T.peek()]:
                        T.pop()
                else:
                    return False 
            index+=1
            
        if T.is_empty() and input_string:
            return True
        else:
            return False

print(Stack.check("(({{]}}))"))

print(Stack.check("{]}"))
                
