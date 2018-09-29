# coding: utf-8


def garage(init, final):
    init = init[::] # 不修改原始init
    step = 0
    process = []
    while init != final:
        index = init.index(0)
        final_index = final[index]
        if final_index != 0:
            exchange_place = init.index(final_index)
            init[index], init[exchange_place] = final_index, 0
        else:
            for i in len(init):
                if init[i] != final[i]:
                    init[i], init[index] = 0, init[i]
                    break
        step += 1
        process.append(init[::])
    return step, process



if __name__ == '__main__':
    i = [1, 3, 5, 0]
    f = [0 , 1, 5, 3]
    s, p = garage(i, f)
    print (s)
    for i in p:
        print (i)










