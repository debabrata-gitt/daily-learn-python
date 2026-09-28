def occurrence(lst, value):
    count = 0

    for i in lst:
        if i == value:
            count += 1

    return count


numbers = [10, 20, 10, 30, 10, 40]

n = int(input("Enter number: "))

print("Occurrence:", occurrence(numbers, n))