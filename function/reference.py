def power(x, n=2):
    return x ** n


def add_end(L=None):
    if L is None:
        L = []
    L.append("end")
    return L


def calc(*numbers): # 可变参数，将传入的参数组装成为一个tuple，使用*来表示
    sum = 0
    for n in numbers:
        sum += n

    numbers = (2,3,4)
    return sum

def person(name,age,**kw):# 关键字参数，转变为dict
    print("name",name,"age",age,"other",kw)
    kw.pop("city")

# 使用可变参数和不可变参数均为解决可变量list与dict之间传地址和传值的问题

person("wang",12,city="boston")

extra = {"city":"bostom","grandfather":"ye"}

person("wang",15,**extra)
print(extra)

# 命名关键字参数的作用是使可变参数有固定的空间

tuple1 = (1,2,3,4,5)
print(calc(*tuple1))
print(tuple1)
# print(power(2, 4))

# 总结 总共有五种命名方式
# 1.位置参数
# 2.默认参数
# 3.可变参数（*）
# 4.关键字参数（**）
# 5.命名关键字参数（*）
