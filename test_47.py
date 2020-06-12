#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:54:04 2020

@author: yl
"""


class Triangle(object):
    def __init__(self):
        self.l = [2, 8, 6, 1, 78, 45, 34, 2]
    def dispose(self, n):
        for i in range(n):
            self.l.insert(0, self.l.pop())
            
        print(self.l)

t = Triangle()
t.dispose(5)
 
if __name__ == '__main__'  :         
    from collections import deque
    
    m = 3
    a = [x for x in range(1,8)]
    f = deque(a)
    f.rotate(m)
    print(list(f))