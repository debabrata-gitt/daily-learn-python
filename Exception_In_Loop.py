numbers = [10, 0, 5, 0, 2]

for num in numbers:
    try:
        print("Result:", 100 / num)

    except ZeroDivisionError:
        print("Cannot divide by zero")