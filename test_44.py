#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:15:11 2020

@author: yl
"""

class Prime(object):
    def dispose(self):
        for i in range(3,101):
            for j in range(2, i):
                if i % j == 0:
                    yield i
                    break
    
    def result(self):
       r = set(range(2,101)) - set(list(self.dispose()))
       print(r)
    
p = Prime()
p.result()