#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:19:02 2020

@author: yl
"""

class Recursion(object):
    
    def __init__(self, s):
        self._strg = s
    
    @property
    def strg(self):
        return self._strg
    
    @strg.setter
    def strg(self, s):
        if isinstance(s, str):
            self._strg = s
        
        else:
            raise ValueError('Enter String')
    
    def dispose(self):
        n = len(self.strg) - 1
        def dis(t = n):
            if t == 0:
                return self.strg[t]
                
                #return self.strg[t]
            print(self.strg[t])
            return dis(t - 1)
        
        return dis
            
r = Recursion('hello world')

rb = r.dispose()

print(rb())
        