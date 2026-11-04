class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age <= 0:
        raise InvalidAgeError("Age must be positive")

    elif age < 18:
        print("You are a minor")

    else:
        print("You are an adult")

except ValueError:
    print("Please enter a valid number")

except InvalidAgeError as e:
    print(e)