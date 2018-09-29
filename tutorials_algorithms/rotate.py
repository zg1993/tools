# coding: utf8
from collections import defaultdict


def rotate_v1(array, k):

    lenght = len(array)
    k = k % lenght
    result = []
    for index, i in enumerate(array):
        if index < lenght - k:
            result.append(i)
        else:
            result.insert(k - lenght, i)
    return result


def rotate_v2(array, k):
    lenght = len(array)
    k = k % lenght
    return array[lenght - k:] + array[: lenght - k]


# 逆序3次，负负得正，只逆序了1-7 8-9 的位置
def rotate_v3(array, k):
    lenght = len(array)
    k = k % lenght

    def reverse(arr, a, b):
        while a < b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1

    reverse(array, 0, lenght - k - 1)
    reverse(array, lenght - k, lenght - 1)
    reverse(array, 0, lenght - 1)


if __name__ == '__main__':
    l = list(range(1, 10))
    print (rotate_v2(l, 2))
    print (rotate_v1(l, 2))
    print ((l, 2))
    print (l)
