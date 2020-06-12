#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:41:09 2020

@author: yl
"""

class Factorial(object):
    def factorial(self):
        result = 1
        
        for i in range(2, 21):
            for j in range(1, i):
                    i = i * j
                    
            result += i
        
        print(result)
        
    def factorial_2(self):
        s = 0
        t = 1
        
        for i in range(1,21):
            t *= i
            s += t
        
        print(s)
        

            
        
f = Factorial()
f.factorial()
f.factorial_2()
                
                