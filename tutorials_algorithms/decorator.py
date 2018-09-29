# coding: utf8


from collections import defaultdict
from functools import wraps
import time
# import sys

# if sys.version_info[0] == 2:
#     from __future__ import print_function


def counts(func):
    stat = defaultdict(int)
    func.stat = stat

    @wraps(func)
    def decorator(*args, **kwargs):
        stat[func.__name__] += 1
        return func(*args, **kwargs)
    return decorator


def time_diff(func):

    @wraps(func)
    def wrappers(*args, **kw):
        c0 = time.clock()
        result = func(*args, **kw)
        diff = time.clock() - c0
        print ('{name}->[{diff: 0.8f}]'.format(
            name=func.__name__, diff=diff))
        return result
    return wrappers
