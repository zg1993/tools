# coding: utf8


# python2 在decorator里使用nonlocal关键字

# 这段代码在python2里运行报错, count, total variable referenced before assignment
def make_averager():
    count = 0
    total = 0
    def averager(value):
        total += value
        count += 1
        return total/count
    return averager


def make_averager_v1():
    count = 0
    total = 0
    d = locals()
    def averager(value):
        d['count'] += 1
        d['total'] += value
        return d['total']/d['count']
    return averager
