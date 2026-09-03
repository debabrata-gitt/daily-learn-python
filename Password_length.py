password = input("Enter password: ")

if len(password) < 6:
    print("Weak Password")
elif password.isalnum():
    print("Medium Password")
else:
    print("Strong Password")