#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 07:09:03 2020

@author: yl
"""


class Experiment(object):
    def start(self, n):
        if len(str(n))  > 5:
            return 'is over'
        
        print('%s 位数 ：' % len(str(n)),  end = '')
        for i in str(n)[::-1]:
            print(i, end = ' ')
 
def hello():
    print('hello world')               
#exper = Experiment()
#exper.start(109)
        
        
