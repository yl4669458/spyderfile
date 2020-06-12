#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:09:20 2020

@author: yl
"""

import datetime, time

if __name__ == '__main__':
    
    print(datetime.date.today().strftime('%d-%m-%Y'))
    
    print(time.strftime('%Y-%m-%d' ' %H:%M:%S', time.localtime(time.time())))
    
    m = datetime.date(1941,1,5)
    
    print(m.strftime('%m-%d-%Y'))
    
    print(time.strftime('%m-%Y-%d' ' %H:%M:%S', time.localtime(time.time())))
    
    print(datetime.date.today().strftime('%m-%d-%Y'))
    
    print(time.strftime('%H:%M:%S', time.localtime(time.time())))
    #替换天
    mb = m + datetime.timedelta(days = 1)
    print(mb.strftime('%Y-%m-%d'))
    #替换年
    miy = m.replace(year = m.year + 1)
    print(miy.strftime('%d-%m-%Y'))
    
    