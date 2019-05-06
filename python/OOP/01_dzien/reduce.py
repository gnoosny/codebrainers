from functools import reduce


X = [1, 2, 3, 4, 5]

print(reduce(lambda a, b: a + b, X))

print(reduce(lambda a, b: a * b, X))