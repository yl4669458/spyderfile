#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 06:53:19 2020

@author: yl
"""

class Year():  
    def __init__(self, *arg):
        if len(arg) > 3:
            raise ValueError('y/m/d')
        self._y, self._m, self._d = arg
        
    @property    
    def month(self):
        self._month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
             7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        return self._month
        
        
    def count_day(self):
        day = 0
        for i in range(1, self._m):
            day += self.month[i]
                
        if self._y / 4 == 0 and self._y % 100 != 0:
            day += self._d + 1
        
        else:
            if self._y % 400 == 0:
                day += self._d + 1
            else:
                day += self._d
            
        print('%s年 %s月%s日  是这年的第%s天' 
              % (self._y, self._m, self._d, day))
        
    
          
        
       
        

y = Year(2015, 6, 7)
y.count_day()


        



        
        
        
            
                
        
        
    
        