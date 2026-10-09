numbers = [3, 5, 6, 10, 12, 15, 20]

result = list(
    filter(lambda x: x % 3 == 0, numbers)
)

print(result)