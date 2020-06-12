#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 07:24:29 2020

@author: yl
"""

"""100000 =>  m * 0.1 = fir
200000 =>  m * 0.075 = scd scd + fir
400000 =>  m * 0.05 = thr scd + fir + thr 
600000 =>  m * 0.03 = fou fir + scd + thr + fou
1000000 => m * 0.015 = fiv fir + scd + thr + fou + fiv
1000000+ => m * 0.01 = six fir + scd + thr + fou + fiv + six

money, fir

for i in range(6):
    if money >= list[i]:
        fir = fir + list[i] * rate[i]
    else:
        if money < list[i]:
            print('销售:%s  奖金:%s ' % (money, fir))
        else:
  """

class Rate(object):
    asse = [1e5, 1e5, 2e5, 2e5, 4e5]
    money = [1e5, 2e5, 4e5, 6e5, 10e5, 10e10]
    inte = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01] 

    def __init__(self):
        m = float(input('Enter money:'))
        if m <= 0:
            raise ValueError('Error, Error')
        self.m = m
        self.cou = 0
        
    def count(self):
        for i in range(6):
            if self.m > self.money[i]:
                self.cou += self.asse[i] * self.inte[i]
                
            else:
                if self.m < 1e5:
                    self.cou = self.m  * self.inte[0]
                    print('销售金额: %s 奖金: %s' % (self.m, self.cou))
                    break
                else:
                    self.cou += (self.m - self.money[i-1]) * self.inte[i]
                    print('销售金额: %s 奖金: %s' % (self.m, self.cou))
                    break

r = Rate()

r.count()
                              
            
            
              
    
