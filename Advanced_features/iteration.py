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
