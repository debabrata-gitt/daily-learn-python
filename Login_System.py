class LoginError(Exception):
    pass

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin" or password != "1234":
        raise LoginError("Invalid username or password")

    print("Login successful!")

except LoginError as e:
    print(e)

finally:
    print("Login process completed")