#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:24:00 2020

@author: yl
"""

class Age(object):
    def five_men(self, n):
        if n == 1:
            return 10
        
        return 2 + self.five_men(n - 1)
    
age = Age()
print(age.five_men(5))
        