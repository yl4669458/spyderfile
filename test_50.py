#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:25:01 2020

@author: yl
"""

class Dic_test(object):
    def dispose(self):
        person = {'yaoyanyi': 8, 'yaoliang': 39, 'chenlu': 34}
        s = []
        for i, j in person.items():
            s.append(j)
        
        s = max(s)
        return s
        
    

d = Dic_test()
print(d.dispose())