# coding: utf8


from collections import defaultdict
from functools import wraps




def count(func):
    cc = 0
    func.bb = cc
    d = defaultdict(int)
    @wraps(func)
    def wrapper(*args, **kw):
        d[func.__name__] += 1
        func.bb += 1
        return func(*args, **kw)
    wrapper.d = d

    return wrapper


class Count:

    def __get__(self, instance, cls):
        print (1111, instance, cls)
        print (1111, self)
        return self[instance.__name__]

    @count
    def fun(self):
        pass

    def l(self):
        f = getattr(self, 'fun', None)
        print (f.bb)

@count
def hello():
    pass


if __name__ == '__main__':
    hello()
    print (hello.d)
    print (dir(hello))
    c = Count()
    print (dir(c.fun))
    c.l()
    # print (hello.c)
