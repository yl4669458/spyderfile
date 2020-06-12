#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:13:10 2020

@author: yl
"""

class Recursion_2(object):
        
    def sort(self, s):
        if len(s) == 1:
            return s[len(s) - 1]
        print(s)
        return s[len(s) - 1] + self.sort(s[:len(s) - 1])
    
r = Recursion_2()
print(r.sort('abcdefghijklmn'))
            
        