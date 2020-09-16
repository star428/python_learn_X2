# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）。
def findMinAndMax(L):
    if not L:
        return None, None
    else:
        min = L[0]
        max = L[0]
        for num in L:
            if num >= max:
                max = num
            if num <= min:
                min = num

        return min, max

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
