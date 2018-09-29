# coding: utf8


from collections import defaultdict
import itertools 


def anagram(s1, s2):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i, j in itertools.zip_longest(s1, s2, fillvalue=None):
        d1[i] += 1
        d2[j] += 1
    print (d1)
    print (d2)
    return d1 == d2

def anagram_v1(s1, s2):
    l1 = [0] * 26
    l2 = [0] * 26
    asc = ord('a')
    for i in s1:
        index = ord(i) - asc
        l1[index] += 1
    for i in s2:
        index = ord(i) - asc
        l2[index] += 1
    return l1 == l2


if __name__ == '__main__':
    print (anagram('afab', 'faa'))
    print (anagram_v1('afa', 'faaa'))
