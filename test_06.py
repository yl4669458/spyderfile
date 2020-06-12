#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:02:39 2020

@author: yl
"""

class assembly(object):
    
    
    def __init__(self, num):
        if num <= 0 or num >=1000:
            raise ValueError('big number 100-999')
        self._num = num 
        self._n = 1
         
    def work(self):
        for i in range(101, self._num + 1):
            if i // 100 != i // 10 % 10:
                if i // 10 % 10 != i % 10 % 10:
                    self.pri(i)
                    
    def pri(self, t):
        if self._n >= 10:
            print(t)
            self._n = 1
        if self._n <= 9:
            print(t, end = ' ')
        self._n += 1
         
    def getnum(self):
        return self._num
    
    def setnum(self, value):
        if value >= 1000 or value <= 0:
            raise ValueError('big number : 100 - 999')
            
        self._num = value
        
    num = property(getnum)
    
    
ass = assembly(999)

ass.work()
    
            
            
        