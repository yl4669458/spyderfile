#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:58:36 2020

@author: yl
"""

class Recursion(object):
    def factorial(self, fun):
        if fun == 1:
            return 1
        
        return fun * self.factorial(fun - 1)
    
r = Recursion()
print(r.factorial(10))
        