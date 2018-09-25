# coding: utf8



def josephus(array, k):
    array = array[::]
    lenght = len(array)
    result = []
    skip = k - 1
    step = 0
    while array:
        step = (step + skip) % lenght
        result.append(array.pop(step))
        lenght -= 1
    return result

def str_josephus(string, k):
    a = [i for i in string]
    lenght = len(string)
    s = ''
    skip = k - 1
    step = 0
    while lenght:
        step = (step + skip) % lenght
        s += a.pop(step)

        lenght -= 1
    return s



if __name__  == "__main__":
    a = '123456789'
    # a = list(range(1, 10))
    # print (josephus(a, 3))
    print (str_josephus(a, 3))


