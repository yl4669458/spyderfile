#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:58:50 2020

@author: yl
"""

class Grade(object):
    def __init__(self, g):
        if  g < 0 or g > 100:
            raise ValueError('grade 1-100')
        self.g = g
    
    def grade(self):
        if self.g >= 90:
            print('A')
            
        elif self.g >= 60 and self.g <= 89:
            print('B')
            
        elif self.g < 60:
            print('C')
            
g = Grade(59)
g.grade()