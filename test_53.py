#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:32:40 2020

@author: yl
"""

class Division(object):
    def dispose(self, n):
        a = 9
        b = '9'
        
        while True:
            if a % n == 0:
                print('%s / %s = %s' % (a, n, a / n))
                break
            
            else:
                a = str(a)
                a += b
                a = int(a)
                
                

d = Division()
d.dispose()
            
            
        