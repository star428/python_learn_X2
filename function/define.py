import math


def drop():
    print("i am drop")


def my_sin(number):
    if not isinstance(number, (int, float)):
        raise ValueError("it's not number")
    else:
        return math.sin(number)


print(my_sin(45))
print(math.pi)
