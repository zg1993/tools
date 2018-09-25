# coding: utf8




# def norepeat(s):
#     long_str = ''
#     l = []
#     for i in range(len(s)):
#         ss = s[i:]
#         if len(ss) < len(long_str):
#             break
#         temp = ''
#         for j in range(len(long_str), len(ss)):
#             if len(set(ss[:j])) != len(ss[:j]):
#                 break
#             temp = ss[:j]
#         if len(temp) > len(long_str):
#             long_str = temp

#     return long_str1

def advanced(string):
    max_lenght = 0
    j = 0
    d = {}
    longest = ''
    for i in range(len(string)):
        if string[i] in d:
            j = max(d[string[i]], j)
        d[string[i]] = i + 1
        if max_lenght < i - j + 1:
        #     print (string, j, i)
            longest = string[j:i+1]
        max_lenght = max(max_lenght, i - j + 1)

    return max_lenght, longest


if __name__ == '__main__':
    s = 'abcabcbb'
    print (s)
    # print (norepeat(s))
    print (advanced(s))
    # print ({1, 2,2,1} == {1, 2, 2})


    # print (list(range(2, 4)))
