#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:53:59 2020

@author: yl
"""

class A():
    class_name = None
    
    def __init__(self):
        print(A.class_name)
        
class B(A):
    class_name = 10
    
    def __init__(self):
        
        print( self.class_name)
        
b = B()
     
        
     

    
  
  
        
        
        