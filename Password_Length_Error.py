class PasswordError(Exception):
    pass

try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise PasswordError("Password must contain at least 8 characters")

    print("Password accepted")

except PasswordError as e:
    print(e)