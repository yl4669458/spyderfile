#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 06:57:16 2020

@author: yl
"""

class Accumulation(object):
    def __init__(self, n):
        if n <=  0 or n >= 10:
            raise  ValueError('Enter 1-9')    
        self.n = n
        
    def dispose(self):
        count = 0
        t = 1
        
        while t < self.n + 1:
            count += int(str(self.n) * t)
            
            if t < self.n:
                print('%s + ' % (str(self.n) * t), end = '')
            
            elif t == self.n:
                print('%s = %s' % ((str(self.n) * t), count))
            
            t += 1
            
a = Accumulation(2)
a.dispose()
            
        