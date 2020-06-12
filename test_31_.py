#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:26:53 2020

@author: yl
"""


#1,3,5,7,5,3,1
#3,2,1,0,1,2,3


class Rhombus(object):
    def dispose(self):
        b = [1,3,5,7,5,3,1]
        a  =[7,5,3,1,3,5,7]
        
        for i in range(7):
            print(a[i]  * ' ' + b[i]  * '*')

r = Rhombus()
r.dispose()