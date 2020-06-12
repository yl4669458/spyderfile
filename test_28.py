#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 07:28:13 2020

@author: yl
"""

class Peach(object):
    def count(self):
        for i in range(1,10000):
            p = i
            for j in range(9):
                i -= i / 2 + 1
                
            if i == 1:
                print(p)
                break
            
p = Peach()
p.count()

class Peach_2(object):
    def count(self):
        x = 1
        for i in range(9):
            x = (x + 1) * 2
        
        print(x)
        
p = Peach_2()
p.count()
            