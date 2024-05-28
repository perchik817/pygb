def f(x, y):
    if y == 0:
        return 1
    return x * f(x, y - 1)
print(f(5, 3))

