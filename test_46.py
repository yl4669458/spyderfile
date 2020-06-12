#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 07:07:01 2020

@author: yl
"""

class Assembly(object):
    a = [[12,7,3], [4,5,6], [7,8,9]]
    b = [[5,8,1], [6,7,3], [4,5,9]]
    
    def dispose(self):
        row = []
        row_2 = []
        for i, j in zip(self.a, self.b):
            for k, l in zip(i, j):
                row.append(k + l)
            
            row_2.append(row[-3:])
        
        return row_2
            
            
            
        
    
a = Assembly()
print(a.dispose())

                