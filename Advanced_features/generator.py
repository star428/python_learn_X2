# 不必储存所有元素在list中而是根据推算的公式来给出后序的值，
# 达到边运算边推算出后序元素的目的(generator)

generator_one = (x ** 2 for x in range(1, 11))
print(generator_one)
print(next(generator_one))  # 内部指针
for num in generator_one:
    print(num)


def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n += 1
    return "done"


def addBeginEnd(list_):
    list_.insert(0, 0)
    list_.append(0)


def triangles():
    line = 1
    L = [1]
    while True:
        L_output = []
        if line == 1:
            line += 1
            L_output = L[:]
            yield L_output[:]
            addBeginEnd(L)
        else:
            for i in range(len(L) - 1):
                L_output.append(L[i] + L[i + 1])
            L = L_output
            line += 1
            yield L_output[:]
            addBeginEnd(L)


def newTriangle():
    x = [1]
    while True:
        yield x[:]
        x = [1] + [x[i] + x[i + 1] for i in range(len(x) - 1)] + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n += 1
    if n == 10:
        break
print(results)

# generator function注意与函数不同的一点是函数遇到return返回而generator遇到yield中断，
# 再次使用for或者next时会再次返回yield中断处重新开始执行直到遇到函数的边界
