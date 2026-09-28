def average(lst):
    total = 0

    for i in lst:
        total += i

    return total / len(lst)


numbers = [10, 20, 30, 40]

print("Average:", average(numbers))