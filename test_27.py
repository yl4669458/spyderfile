#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:23:32 2020

@author: yl
"""

class Ball(object):
    def __init__(self, metr):
        self.meter = metr
    
    @property
    def meter(self):
        return self._meter
    
    @meter.setter
    def meter(self,  metr):
        if metr <= 0:
            raise ValueError('Enter > 0')
            
        self._meter = metr
        
    def dispose(self):
        count = 0
        
        for i in range(10):
            count += self.meter
            self.meter /= 2
            count += self.meter
            if i == 9:
                print('10 times: %s meter \ntenth jumped: %s' % (count, self.meter))
 
                
ball = Ball(100)
ball.dispose()