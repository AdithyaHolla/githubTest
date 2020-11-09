#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:44:11 2020

@author: adithya
"""
import random

class Print_Queue:
    
    def __init__(self):
        self.items=[]
        
    def enq(self, data):
        self.items.insert(0,data)
        
    def deq(self):
        if self.items:
            return self.items.pop()
        else:
            return None
    
    def size_queue(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
        
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

class Printer:
    
        def get_job(self):
            
            if not self.is_empty():
                print("Printing... Job Number:{}".format(self.peek()))
                self.deq()
            else:
                return TypeError("Error")
        
class Job(Print_Queue, Printer):
    
    def __init__(self):
        
        super().__init__()
        self._lis = list(range(1,random.randint(1,10)+1))
    
        for l in self._lis:
            self.enq(l)
        self._pages = len(self.items)


    def print_page(self):
        
        while len(self.items):
            self.get_job()
            self._pages = self._pages - 1
            self.check_complete()
    
    
    def check_complete(self):
        
        if self._pages:
            print(f"{self._pages} Pages Remaning")
        else:
            print("Printing Job Compelte")

        
def main():
    J = Job()
    J.print_page()

if __name__=="__main__":main()




