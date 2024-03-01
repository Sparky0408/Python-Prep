from functools import reduce


def sum(a, b):
    return a + b


li = [1, 4, 6, 9, 1, 54, 2]

result = reduce(sum, li)

print(result)
