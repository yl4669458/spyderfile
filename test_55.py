#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 18:08:50 2020

@author: yl
"""

class Password(object):
    def dispose(self, p):
        s = []
        n = str(p)
        t = 1
        
        for i in n:
            s.append(int(i) + 5)
            
        for j in range(len(s)):
            s[j] = str(s[j])
            
        for i in range(len(s) // 2):
            s[i], s[len(s) - t] = s[len(s) - t], s[i]
            t += 1
            
            
        s = ','.join(s)
        s = s.replace(',', '')
        return s
        
p = Password()
print(p.dispose(1234))
        