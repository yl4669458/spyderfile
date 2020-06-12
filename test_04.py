#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 07:01:32 2020

@author: yl
"""

class Per(object):
    group = [1,2,3,4]
    
    def assembly(self):
        for i in self.group:
            for j in self.group:
                for k in self.group:
                    if i != j and j != k:
                        print(i,j,k)


class testPer(Per):
    group = [1,2,3,4,5]
    

t = testPer()
t.assembly()
         