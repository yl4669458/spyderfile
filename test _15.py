#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:30:56 2020

@author: yl
"""

import time
class Multip(object):
    def multab(self):
        for i in range(1, 10):
            print()
            for j in range(1, i+1):
                print('%s*%s=%s||' % (i, j, i*j), end = ' ')
                time.sleep(2)
            
m = Multip()
m.multab()