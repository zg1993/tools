# coding: utf8



def n_sum(array, n, target):
    seq = []
    if n == 2:
        return two_sum(array, target)
    array.sort()
    prev = None
    for index, num in enumerate(array):
        if prev is not None and num == prev:
            continue
        result = n_sum(array[index+1:], n-1, target-num)
        if result:
            seq.extend(append_elem_to_each_list(result, num))
        seq = union_seq(seq)
    return seq


def append_elem_to_each_list(result, num):
    seq = []
    if result:
        for i in result:
            i.append(num)
            seq.append(sorted(i))
    return seq


def union_seq(duplicate_seq):
    result = []
    if len(duplicate_seq):
        duplicate_seq.sort()
        result.append(duplicate_seq[0])
        for r in duplicate_seq[1:]:
            if r != result[-1]:
                result.append(r)
    return result



def two_sum(array, target):
    array = sorted(array)
    seq = []
    lt = 0
    rt = len(array) - 1
    while lt < rt:
        s = array[lt] + array[rt]
        if s == target:
            seq.append(sorted([array[lt], array[rt]]))
            while (lt < len(array) and array[lt] == array[lt+1]):
                lt += 1
            while (rt > 0 and array[rt] == array[rt-1]):
                rt -= 1
            lt += 1
            rt -= 1
        elif s > target:
            rt -= 1
        else:
            lt += 1
    return seq


if __name__ == '__main__':
    a = [11, 2, 3, 3, 4, 7, 1,0]
    a = [1, 0, -1, 0, -2, 2]
    target = 0
    n = 4
    print (n_sum(a, n, target))



