#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 08:43:08 2020

@author: yl
"""

from itertools import product

class Groupby(object):
    def dispose(self):
        a = ['a', 'b', 'c']
        b = ['x', 'y', 'z']
        
        for i in product(a, b):
            if (i != ('a', 'x')) and (i != ('c', 'x') and i != ('c', 'z')):
                
                print(i)
                
g = Groupby()
g.dispose()