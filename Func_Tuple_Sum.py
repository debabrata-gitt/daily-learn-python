def tuple_sum(t):
    total = 0

    for i in t:
        total += i

    return total

numbers = (10, 20, 30, 40)

print("Sum:", tuple_sum(numbers))