#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:02:31 2020

@author: yl
"""

class GameObject:
    class_name = ''
    desc = ''
    objects = {}
    
    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self
        
    def get_desc(self):
        return self.class_name + '\n' + self.desc
  
    
class Goblin(GameObject):
    class_name = 'goblin'
    desc = 'A foul creature'
    
 
goblin = Goblin('Gobbly')

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return 'There is no %s here.' % noun
        