# coding: utf8


from tutorials_algorithms.decorator import counts
import pdb


# def add_operator(nums, target):
#     res = []

#     def dfs(nums, target, path, pos, prev, multed):
#         print prev
#         if pos + 1 == len(nums):
#             if prev == target:
#                 res.append(path)
#         cur = int(nums[pos])
#         # print range(pos + 1, len(nums))
#         for i in range(pos + 1, len(nums)):
#             if nums[pos] == 0:
#                 continue
#             else:
#                 add = path + '+' + str(cur)
#                 add_value = prev + cur
#                 red = path + '-' + str(cur)
#                 red_value = prev - cur
#                 mul = path + '*' + str(cur)
#                 mul_value = (prev - multed) * cur + multed
#                 dfs(nums, target, add, pos + 1, add_value, prev)
#                 dfs(nums, target, red, pos + 1, red_value, prev)
#                 dfs(nums, target, mul, pos + 1, mul_value, prev)

#     dfs(nums, target, '', 0, 0, 0)
#     return res
def add_operator(nums, target):
    res = []

    @counts
    def dfs(path, pos, prev, multed):
        pdb.set_trace()
        if pos == len(nums):
            if prev == target:
                res.append(path)
            return
        for i in range(pos, len(nums)):
            if i != pos and nums[pos] == '0':
                break
            cur = int(nums[pos: i + 1])
            if pos == 0:
                dfs(str(cur), i + 1, cur, cur)
            else:
                add = path + '+' + str(cur)
                red = path + '-' + str(cur)
                mul = path + '*' + str(cur)
                dfs(add, i + 1, prev + cur, cur)
                dfs(red, i + 1, prev - cur, -cur)
                dfs(mul, i + 1, prev - multed + cur * multed, cur * multed)
    dfs('', 0, 0, 0)
    print dfs.stat
    return res


if __name__ == '__main__':
    res = add_operator('102', 24)
    print res
