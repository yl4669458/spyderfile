#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:34:31 2020

@author: yl
"""

if __name__ == '__main__':
    import time
    start = time.time()
    
    for i in range(3000):
        print(i)
    
    end = time.time()
    
    print(end - start)
    
import pymongo


