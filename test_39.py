#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:06:15 2020

@author: yl
"""
from test_38 import hello

def test_hello(n):
    for i in range(n):
        hello()
        
t = test_hello(5)


