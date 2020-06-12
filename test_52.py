#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:35:51 2020

@author: yl
"""

class Hahaqi(object):
    def dispose(self):
        from itertools import permutations

        r = 0
        for i in permutations('12345670'):
            n = list(i)
            n = ','.join(n)
            n = n.replace(',', '')
            n = int(n)
            
            if n % 2 != 0:
                r += 1
        
        return r
        
h = Hahaqi()
print(h.dispose())