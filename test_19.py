#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:27:09 2020

@author: yl
"""

class Factor(object):
    def __init__(self, f):
        self.num = f
            
    def dispose(self):
        for i in range(2, 10):
            for j in range(2, i+1):
                for k in range(2, j+1):
                    for l in range(2, k+1):
                        if i * j * k * l == self.num:
                                print('%s * %s * %s * %s = %s' % (i,j,k,l,self.num))
                            

f = Factor(80)
f.dispose()