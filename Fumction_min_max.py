def max_min(lst):
    maximum = lst[0]
    minimum = lst[0]

    for i in lst:
        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    return maximum, minimum


numbers = [10, 5, 30, 2, 50]

maximum, minimum = max_min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)