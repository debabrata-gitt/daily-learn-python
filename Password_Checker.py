password = input("Enter password: ")

if len(password) >= 8:
    print("Password length is valid")
else:
    print("Password is too short")