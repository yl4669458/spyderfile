#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 07:36:44 2020

@author: yl
"""
class Assembly(object):
    def dispose(self):
        for i in range(10, 100):
            if i * 809 >= 1000 and i * 809 < 10000:
                if i * 8 < 100:
                    if i * 9 >=100 and i * 9 < 1000:
                        print(i, 809 * i)
 

a = Assembly()
a.dispose()