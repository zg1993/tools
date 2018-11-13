# coding: utf8


<<<<<<< HEAD
from base64 import b64encode
from functools import partial


def fun(a, b=None, c=None):
  print a,b,c
  print ';' , b

  print 'c', c

f = partial(fun, 'dsfaf', c='dfsaf')
f()


# l1 = filter(lambda i:i.get('status') == '0', l)
# # print len(l)
# r = []
# for i in l:
#     if i.get('status') == 0 and i.get('role') == 1:
#         r.append(b64encode("0"+"_"+ i.get('phone')))
#
# print r

'''
Given a matrix of words and a list of words to search,
return a list of words that exists in the board
This is Word Search II on LeetCode
board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']
         ]
words = ["oath","pea","eat","rain", "egg"]
'''


def find_words(board, words):

    def backtrack(board, i, j, trie, pre, used, result):
        '''
        backtrack tries to build each words from
        the board and return all words found
        @param: board, the passed in board of characters
        @param: i, the row index
        @param: j, the column index
        @param: trie, a trie of the passed in words
        @param: pre, a buffer of currently build string that differs
                by recursion stack
        @param: used, a replica of the board except in booleans
                to state whether a character has been used
        @param: result, the resulting set that contains all words found
        @return: list of words found
        '''

        if '#' in trie:
            result.add(pre)

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        if not used[i][j] and board[i][j] in trie:
            used[i][j] = True
            backtrack(board, i+1, j, trie[board[i][j]],
                      pre+board[i][j], used, result)
            backtrack(board, i, j+1, trie[board[i][j]],
                      pre+board[i][j], used, result)
            backtrack(board, i-1, j, trie[board[i][j]],
                      pre+board[i][j], used, result)
            backtrack(board, i, j-1, trie[board[i][j]],
                      pre+board[i][j], used, result)
            used[i][j] = False

    # make a trie structure that is essentially dictionaries of dictionaries
    # that map each character to a potential next character
    trie = {}
    for word in words:
        curr_trie = trie
        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            curr_trie = curr_trie[char]
        curr_trie['#'] = '#'
    print trie

    # result is a set of found words since we do not want repeats
    result = set()
    used = [[False]*len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            backtrack(board, i, j, trie, '', used, result)
    return list(result)

board = [
         ['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']
         ]
words = ["eat", "egg"]
# words = ["oath","pea","eat","rain", "egg"]

print find_words(board, words)
=======
from collections import defaultdict
from functools import wraps




def count(func):
    cc = 0
    func.bb = cc
    d = defaultdict(int)
    @wraps(func)
    def wrapper(*args, **kw):
        d[func.__name__] += 1
        func.bb += 1
        return func(*args, **kw)
    wrapper.d = d

    return wrapper


class Count:

    def __get__(self, instance, cls):
        print (1111, instance, cls)
        print (1111, self)
        return self[instance.__name__]

    @count
    def fun(self):
        pass

    def l(self):
        f = getattr(self, 'fun', None)
        print (f.bb)

@count
def hello():
    pass


if __name__ == '__main__':
    hello()
    print (hello.d)
    print (dir(hello))
    c = Count()
    print (dir(c.fun))
    c.l()
    # print (hello.c)
>>>>>>> cfc190a709a8f79821b4b16df35c612fa62ad3b8
