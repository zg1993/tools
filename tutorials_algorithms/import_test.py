# coding: utf8

from __future__ import absolute_import, division
import decorator
from decorator import time_diff
# decorator.time_diff
# decorator.counts(lambda x:x)
# print 1/3

@time_diff
def fun(a=None, b=None, c=None, **kwargs):
    print a, b,c 

@time_diff
def fun1(info):
    print info['a']
a=1
b=2
c=3
d = {'a': 11, 'b': 324, 'c': 122}
# fun(a=a,b=b,c=c)
fun(**d)
fun1(d)

