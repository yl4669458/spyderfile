#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:51:05 2020

@author: yl
"""

class Fib(object):
    def __init__(self, n):
        self.num = n
        
    def seq(self):
        a, b = 0, 1
        for i in range(self.num):
            a, b = b, a+b
        print(a)
f = Fib(1)
f.seq()