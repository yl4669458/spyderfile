#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:35:34 2020

@author: yl
"""

class Prime(object):
    def __init__(self, num):
        if not num > 1:
            raise ValueError('请输入大于1的正整数')
            
        self.num = num

    def dispose(self):
        p = []
        n = self.num
        while self.num != 1:
            for i in range(2, self.num + 1):
                if self.num % i == 0:
                    p.append(i)
                    self.num //= i
                    break
       
        for i in range(len(p)):
            if i == len(p) - 1:
                print('%s = %s' % (p[i], n))
            else:
                print('%s * ' % p[i], end = '')
        
                
p = Prime(10000)
p.dispose()