#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:02:00 2020

@author: yl
"""

def count():
    num = []
    for m in range(1, 168):
        for n in range(m):
            if m*m - n*n == 168:
                num.append(n*n - 100)
    print(num)

c = count()