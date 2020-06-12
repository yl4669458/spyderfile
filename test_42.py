#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:18:29 2020

@author: yl
"""

def hello_world():
    print('hello world')
    
def three_hellos():
    for i in range(3):
        hello_world()
        
if __name__ == '__main__':
    three_hellos()
            
 