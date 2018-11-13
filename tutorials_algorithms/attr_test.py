# coding: utf8



class A(object):
    name = 'z'

    def __getattr__(self, name):
        print '__getattr__'

    def __getattribute__(self, name):
        print '__getattribute__'
        raise AttributeError

    def __getitem__(self, key):
        print key