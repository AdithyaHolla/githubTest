#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:52:01 2020

@author: adithya
"""

class DLLNode:
    
    def __init__(self, data):
        self.data = data 
        self.next = None 
#        self.previous = None
    
    def __repr__(self):
        return "Node object: data={}".format(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data 
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next 
        
#    def get_previous(self):
#        return self.previous 
#        
#    def set_previous(self, new_node):
#        self.previous = new_node
        
class List:
    
    def __init__(self):
        self.head = None 
        
    def __repr__(self):
        return "SLL Obj = {}".format(self.head)
    
    def is_empty(self):
        if self.head == None:
            return True 
        else:
            return False
    
    def add_f(self, new_data):
        temp = DLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp 
        
    def size(self):
        size = 0
        if self.head == None:
            return 0 
        current = self.head 
        
        while current != None:
            size += 1
            current = current.get_next()
        
        return size 
    
    def search(self, s_data):
        if self.head == None:
            return "LL is Empty"
        
        current = self.head 
        
        while current != None:
            if current.get_data() == s_data:
                return True
            else:
                current = current.get_next()
                
        return False
        
    def remove(self, r_data):
        if self.head is None:
            return "The LL is empty"
        
        current = self.head
        prev = None
        found = False 
        
        while not found:
            if current.get_data() == r_data:
                found = True
            else: 
                if current.get_next() is None:
                    return "Not present"
                else:
                    prev = current
                    current = current.get_next()
            
        if prev is None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())
                    