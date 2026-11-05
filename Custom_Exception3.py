class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError("Negative number is not allowed")

    print("Number:", num)

except ValueError:
    print("Please enter a valid integer")

except NegativeNumberError as e:
    print(e)