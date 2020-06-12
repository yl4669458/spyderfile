#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:48:11 2020

@author: yl
"""

class Rate(object):
    money = [1e6, 6e5, 4e5, 2e5, 1e5, 0]
    inte = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    
    def __init__(self):
        m = float(input('Enter money:'))
        if m < 0:
            raise ValueError('Error,Error,Enter positive number')
        
        self.m = m
        self.m1 = m
        self.cou = 0
    
    def count(self):
        for i in range(6):
            if self.m > self.money[i]:
                self.cou += (self.m - self.money[i]) * self.inte[i]
                self.m = self.money[i]
                
        print('销售额: %s  提成金额: %s' % (self.m1, self.cou))
        
        
r = Rate()
r.count()
        
    