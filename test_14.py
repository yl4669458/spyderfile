#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:12:37 2020

@author: yl
"""

import time


def dic():
    d = {'jam': 90, 'mac': 20}
    l = list(d.items())
    
    s = sorted(l, key = lambda x : x[:1])
    
    s = dict(s)
    time.sleep(2)
    print(s)
   
d = dic()