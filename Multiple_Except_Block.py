try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)

except ValueError:
    print("Please enter integers")

except ZeroDivisionError:
    print("Cannot divide by zero")