from functools import reduce

lists = [[1, 2], [3, 4], [5, 6]]

result = reduce(lambda a, b: a + b, lists, [])

print(result)