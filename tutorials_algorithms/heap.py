# coding: utf8

from random import randint

ll = [randint(1,199) for i in range(10)]



def insert(l, size, element):
    l.append(element)
    while True:
        if size < 1:
            break
        parent = (size-1)/2
        if element >= l[parent]:
            break
        else:
            l[size] = l[parent]
            size = parent
    l[size] = element

def insert_advanced(l, size, element):
    l.append(element)
    if size == 0:
        return
    parent = (size-1) >> 1
    while parent >= 0 and l[parent] < element:
        l[size] = l[parent]
        size = parent
        
    

def pop_advanced(l, size):
    min_value = l[0]
    place = 0
    while (place+1)*2 < size:
        r_child = (place+1)*2
        if r_child - 1 != size and l[r_child] < l[r_child-1]:
            child = r_child
        else:
            child = r_child -1
        l[place] = l[child]
        place = child
    l[place]= l[-1]
    l.pop()
    return min_value

def pop(l, size):
    assert size != 0
    min_value = l[0]
    temp = l[-1]
    parent = 0
    while True:
        if parent+1 >= size:
          #  print 'parent, size',parent + 1, size
            
            break
        right_child = (parent+1) * 2
        left_child = right_child - 1
        if left_child >= size:
           #  print 'right', right_child
             break
        if size > right_child and l[right_child] < l[left_child]:
 #          
            child = right_child
        else:
 #           print 'left',left_child
            child = left_child
  #      print 'child', child
        l[parent] = l[child]
        parent = child
   # print 'l: ', l
    #print 'parent: ', parent
    l[parent] = temp
    l.pop()
    print 'after: ', l
    return min_value
    
def main():
    l1 = []
    l2 = []
    for i in ll:
        insert(l1, len(l1), i)
    print l1
    for _ in range(len(l1)):
        l2.append(pop_advanced(l1, len(l1)))
    print l2
    

if __name__ == '__main__':
    print ll
    main()
    
