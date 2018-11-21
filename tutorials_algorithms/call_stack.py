# coding: utf8 



import inspect

def a():
    b()

def b():
    c()

def c():
    stack = inspect.stack()



a()