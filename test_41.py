#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:40:04 2020

@author: yl
"""

class Inspection(object):
    week_1 = ['Monday', 'Wenseday', 'Friday', 'Tuseday', 'Thursday', 'Saturday', 'Sunday'] 
    week_2 = ['Tuseday', 'Thursday', 'Saturday', 'Sunday']
       
    def check(self):
        m = input('Enter first letter:')
        m = m[:1].upper() + m[1:].lower()
        n = 0
        
        for i in self.week_1:
              for j in self.week_2:
                  if m in j:
                      if len(m) == 1:
                          p = input('second letter:')
                          m += p.lower()
                      if m in j:
                         n += 1
                         return print(j)
              if m in i:
                  n += 1
                  print(i)
        
        if n == 0:
            self.check()
            
            
inspe = Inspection()
inspe.check()                        
            
                   
                         
                     
        
                
       
            
                       
                        