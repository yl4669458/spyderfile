#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:41:02 2020

@author: yl
"""

class Statistics(object):
    def __init__(self, s):
        self.s = s
    
    def dispose(self):
        letter = 0
        space = 0
        digit = 0
        for i in self.s:
            if i.isalpha():
                letter += 1
                
            elif i.isspace():
                 space += 1
                 
            elif i.isdigit():
                 digit += 1
                 
        print('char:%s \nletter:%s  space:%s  digit:%s' % 
                  (self.s, letter, space, digit))
        
s = Statistics('hello world 520 1314')
s.dispose()
             
                