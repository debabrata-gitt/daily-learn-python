def is_valid(n):
    return n > 0 and n % 5 == 0


numbers = [10, -5, 15, 0, 22, 25]

result = list(filter(is_valid, numbers))

print(result)