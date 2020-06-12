#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:32:05 2020

@author: yl
"""

class Arrange(object):
    def __init__(self, *arg):
        self.ret = arg
        self.ret = list(self.ret)
    
    def assembly(self):
        print(sorted(self.ret))
    
class Arr(Arrange):
    def ass(self):
        self.ret = self.ret.sort()
        for i in self.ret:
            print(i, end = ' ')
                
arr = Arr(12,5,4,8,9,6,3,45)
arr.ass()
            
                    
                
                
                