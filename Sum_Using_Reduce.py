from functools import reduce

numbers = [10, 20, 30, 40, 50]

result = reduce(lambda a, b: a + b, numbers)

print("Total:", result)