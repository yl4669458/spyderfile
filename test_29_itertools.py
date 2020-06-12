#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 09:39:37 2020

@author: yl
"""

import itertools

print('accumulate')
x = itertools.accumulate(range(2, 10), lambda x, y: x * 10 + y)

l = list(x)
print(l)



class Test(object):
    
    def test_2(self):
       return map(lambda x, y : x == y, range(10), range(5))
    


t = Test()

#for i in t.test(10):
#    print(i)
    
print(list(t.test_2()))

#chain
print('chain')
a = itertools.chain(range(4),range(18,27),['a'],('b'))
print(list(a))


#combinations_with_replacement
print('combinations_with_replacement')
y = itertools.combinations_with_replacement('123', 2)
for i in y:
    print(i)
    
#product
print('product')
z = itertools.product('abc', 'xyz','123')
for i in z:
    print(i, )
    
#permutations
print('permutations')
p = itertools.permutations('123')
for i in p:
    print(i)
    
#combinations 
print('combinations')
b = itertools.combinations('123', 2)
print(list(b))

#repeat
print('repeat')
j = itertools.repeat({1:'2'}, 5)

for i in j:
    print(i)
    
#tee
print('tee')
f = itertools.tee(range(10), 5)
for i in f:
        print(list(i))


#count
c = itertools.count(15, -1)
print('count')
for i in itertools.islice(c, 10):
    print(i, )
print()   
#cycle
print('cycle')
x = itertools.cycle('ABC')

for i in itertools.islice(x, 10):
    print(i)
   
#groupby
print('groupby')

x = itertools.groupby(range(10), lambda x: x < 5 or x > 8)
for condition, numbers in x:
    print(condition, list(numbers))