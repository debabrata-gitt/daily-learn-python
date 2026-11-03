def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 0))
print(divide(20, 5))