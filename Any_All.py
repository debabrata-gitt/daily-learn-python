numbers = [2, 4, 6, 7, 8]

print(any(x % 2 != 0 for x in numbers))
print(all(x > 0 for x in numbers))