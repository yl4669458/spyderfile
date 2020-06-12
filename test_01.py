#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 08:16:07 2020

@author: yl
"""

class revealAccess:
    x = 4
    y = 10
    def __init__(self, initval = None, name = 'var'):
        self.val = initval
        self.name = name
    
    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val
    
    def __set__(self, obj, val):
        print('updating', self.name)
        self.val = val
        

r = revealAccess()
r.x
#m = revealAccess(20, 'hello')
#m.x
#感想，__get__, __set__, 
#定义这两个方法的类的实例触发不了这两个方法的自动执行
#用其他的类来调用和修改，定义了这两个方法的类的实例会触发自动执行
