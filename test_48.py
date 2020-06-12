#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 07:01:01 2020

@author: yl
"""

class Numbers(object):
    def dispose(self, n):
        s = 0
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                s += 1/i
        else:
            for i in range(1, n + 1, 2):
                s += 1/i
         
        return s
num = Numbers()
n = num.dispose(6)
print(n)            
            