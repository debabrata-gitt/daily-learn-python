from functools import reduce

numbers = [10, 50, 20, 90, 30]

result = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("Maximum:", result)