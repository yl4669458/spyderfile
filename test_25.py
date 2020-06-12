#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:34:13 2020

@author: yl
"""

class Accumulation(object):
    def __init__(self, n):
        if n <= 0 or n >= 10:
            raise ValueError(' Enter 1--9')
      
        self.n = n
        
    def dispose(self):
        default = '2'
        count = 0
        t = 1
        
        while self.n + 1 > t:
            count += int(default * t)
            
            if t < self.n:
                print('%s + ' % (default * t), end = '' )
                
            else:
                print('%s = %s' % (default * t, count))
                
            t += 1
            
a = Accumulation(5)
a.dispose()        
        