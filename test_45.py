#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:49:21 2020

@author: yl
"""
class Static(object):
    StaticVar = 5
    
    def  varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)
        

print(Static.StaticVar)

a = Static()
for i in range(3):
    a.varfunc()
    
print(Static.StaticVar)