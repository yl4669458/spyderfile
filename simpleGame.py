#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 06:56:40 2020

@author: yl
"""

def get_input():   
     command = input(': ').split()
     verb_word = command[0]
     if verb_word in verb_dict:
         verb = verb_dict[verb_word]
     else:  
         print('Unknown verb %s' % verb_word)
         return
     
     if len(command) >= 2:
         noun_word = command[1]
         print(verb(noun_word))
     else:
         print(verb('nothing'))

def say(noun):
    return 'You said "%s"' % noun

def hit(noun):
    return 'You hited "%s"' % noun

verb_dict = {
    'say' : say,
    'hit' : hit
    }

#while True:
#    get_input()
         

class GameObject:
    class_name = ''
    decs = ''
    objects = {}
    
    