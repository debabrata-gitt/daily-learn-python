def add(*numbers):
    total = 0

    for i in numbers:
        total += i

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))