from itertools import groupby

numbers = [1, 1, 2, 2, 2, 3, 4, 4]

for key, group in groupby(numbers):
    print(key, list(group))