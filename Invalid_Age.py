class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

    elif age < 18:
        print("You are not eligible to vote")

    else:
        print("You are eligible to vote")

except ValueError:
    print("Please enter a valid number")

except InvalidAgeError as e:
    print("Error:", e)

finally:
    print("Age verification completed")