def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


# test
move(3, "a", "b", "c")
