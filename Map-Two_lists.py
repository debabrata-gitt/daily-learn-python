def add(a, b):
    return a + b


list1 = [10, 20, 30]
list2 = [1, 2, 3]

result = list(map(add, list1, list2))

print(result)