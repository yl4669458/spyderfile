#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:26:43 2020

@author: yl
"""

from test_38 import Experiment

class Times(Experiment):
    def times(self):
        n = input('Enter number:')
        if n == n[::-1]:
            print('Yes yes is Times')
            
        else:
            print('No no is not Times')
            
t = Times()
t.times()
        

