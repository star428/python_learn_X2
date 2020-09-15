list_one = [0, 1, 2, 3, 4, 5]
print(list_one[:3])
print(list_one[-2:])
list_two = [x for x in range(100)]
print(list_two[::5])


def trim(s):
    length = len(s)
    beginStr = 0
    endStr = -1
    if length == 0:
        return s
    else:
        for x in range(length):
            if s[x] == " ":
                pass
            else:
                beginStr = x
                break

        for x in range(length-1, -1, -1):
            if s[x] == " ":
                pass
            else:
                endStr = x
                break

        return s[beginStr:endStr+1]

# 使用尾递归求解
def newTrim(s):
    if s == "":
        return s
    elif s[0] == " ":
        s = s[1:]
    elif s[-1] == " ":
        s = s[:-1]
    else:
        return s
    return newTrim(s)




if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
