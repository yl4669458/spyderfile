#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:16:02 2020

@author: yl
"""

from itertools import accumulate
from itertools import chain



class Decimals(object):
    def dispose(self):
        a, b = 1, 2
        c, d = 1, 1
        result = 0
        
        
        for i in range(20):
            a, b = b, a + b
    
            c, d = d, c + d
            
            result  += a / c
            
        print(round(result, 2))
            
d = Decimals()
d.dispose()

class Deci(object):
    def dispose(self):  
        a = chain([1,1,1],range(2,18))
        b = accumulate(a)
        
        for i in b:
            print(i)
            
deci = Deci()
deci.dispose()
    