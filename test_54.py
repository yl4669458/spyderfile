#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:03:32 2020

@author: yl
"""

class Stamp(object):
    def dispose(self, n):
        s = n * '*'
        print('%s print %s' % (n, s))
        
s = Stamp()
s.dispose(8)
        