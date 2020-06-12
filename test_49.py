#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:18:44 2020

@author: yl
"""

class Listoutput(object):
    def dispose(self):
        from itertools import cycle
        import time
        l = ['yaoyanyi', 'chenlu', 'yaoliang']
        
        for i in cycle(l):
            print(i)
            time.sleep(1)
            
lis = Listoutput()
lis.dispose()