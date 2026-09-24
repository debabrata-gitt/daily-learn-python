numbers = [float(value) for value in input("Enter li5st elements separated by spaces: ").split()]

if not numbers:
    print("The list is empty.")
else:
    numbers.sort()
    middle = len(numbers) // 2

    if len(numbers) % 2:
        median = numbers[middle]
    else:
        median = (numbers[middle - 1] + numbers[middle]) / 2

    print("Median:", median)