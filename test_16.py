#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:49:18 2020

@author: yl
"""

import time

def test_time():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print(time.localtime(time.time()))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    
t = test_time()