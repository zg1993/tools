# coding: utf8

from decorator import counts


@counts
def sum_array(array, target, n):
    # array = sorted(array)
    result = []
    if n == 1:
        for num in array:
            if num == target:
                result.append([num])
                break
        return result
    else:
        for index, num in enumerate(array, 1):
            seq = sum_array(array[index:], target-num, n-1)
            if seq:
                result += append_seq(num, seq)
    return result


def append_seq(num, seq):
    result = []
    for i in seq:
        i.append(num)
        result.append(sorted(i))
    return result


def remove_duplicate(seq_duplicate):
    seq_duplicate = sorted(seq_duplicate)
    result = [seq_duplicate[0]]
    for seq in seq_duplicate[1:]:
        if seq != result[-1]:
            result.append(seq)
    return result


if __name__ == '__main__':
    a = range(0, 11) + [1, 2]
    # a = [1, 0, -1, 0, -2, 2]
    target = 9
    # target = 0
    n = 2
    # n = 4
    print sum_array.__name__
    result = sum_array(a, target, n)
    print dir(sum_array)
    result = remove_duplicate(result)
    print result
