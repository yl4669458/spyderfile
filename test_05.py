#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 08:25:13 2020

@author: yl
"""

class A(object):
    
    def __init__(self, gir):
        self._group = gir
    
    @property
    def group(self):
        return self._group
    
    @group.setter
    def group(self, g):
        if g >= 100 or g <= 0:
            raise ValueError('Number is too big')
            
        self._group = g

a = A(100)
     
    
class B(object):
    def __init__(self, g = 10):
        self._group = g
        
    def getgroup(self):
        return self._group
    
    #def setgroup(self, g):
     #   if g <= 0 or g >=100:
        #    raise ValueError('big number 1-99')
       # self._group = g
        
    group = property(getgroup)
    
    
b = B()
print(b.group)
b.group =1000