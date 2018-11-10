# coding: utf8
from collections import deque
# from functools import iter
# from itertools import iter
import itertools

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    
    # print (list(it))  
    d = deque(itertools.islice(it, n-1))                                            
    # print (list(it))
    # print (d, list(it))
    d.appendleft(0)
    s = sum(d)

    for elem in it:
        s += elem - d.popleft()
        print (s, elem)
        d.append(elem)

        yield s / float(n)

print (list(moving_average([40, 30, 50, 46, 39, 44])))

