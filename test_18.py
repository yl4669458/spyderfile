#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 06:57:33 2020

@author: yl
"""

import time
class Daffodil(object):
    
    def dispose(self):
        for i in range(100, 1000):
            if (i // 100)**3 + (i//10%10)**3 + (i % 10 % 10)**3 == i:
                time.sleep(2)
                print(i, end = ' ')
                
d = Daffodil()
d.dispose()