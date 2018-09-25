# coding: utf-8
'''
给一个list和一个数字N，生成一个新的list包含每个元素最多出现N次
'''
import collections


# Time complexity O(n^2)
def delete_nth_native(array, n):
    
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


# Time complexity O(n) element must be hash
def delete_nth(array, n):
    ans = []
    count = collections.defautldict(int)
    for num in array:
        if count[num] < n:
            ans.append(num)
            count[num] +    = 1
    return ans




