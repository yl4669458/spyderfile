#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:21:27 2020

@author: yl
"""

class Ball(object):
   def __init__(self, m):
       self.meter = m
             
   @property 
   def meter(self):
        return self._meter
    
   @meter.setter 
   def meter(self, m):
        if m <= 0:
            raise ValueError('Enter > 0')
            
        self._meter = m
        
        
ball = Ball(100)
print(ball.meter)
ball.meter = 50
print(ball.meter)