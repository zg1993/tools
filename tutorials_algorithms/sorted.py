# coding: utf8

l = [2, 3, 10, 11, 1, -1, 111, 8, 7, 6]

def segmentation(array, start, end):
    if start < end:
        base = array[start]
        while start != end:
            while start != end:
                if array[end] > base:
                    end -= 1
                else:
                    array[start] = array[end]
                    start += 1
                    break
            while start != end:
                if array[start] < base:
                    start += 1
                else:
                    
                    array[end] = array[start]
                    end -= 1
                    break
        array[start] = base
        return start

    
def partition(array, start, end):
    place = start
    base = array[start]
    while start <= end:
        if array[start] < base:
            temp = array[start]
            array[start] = array[place+1]
            array[place] = temp
            place += 1
        start += 1
    array[place] = base
    return place

def quick_sorted(array, start, end):
    if end > start:
#        place = segmentation(array, start, end)
        place = partition(array, start, end)
        quick_sorted(array, start, place)
        quick_sorted(array, place+1, end)

    

if __name__ == '__main__':
    print l
    quick_sorted(l, 0, len(l)-1)
    print l
