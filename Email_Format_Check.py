import re

email = input("Enter your email: ")

pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"

if re.fullmatch(pattern, email):
    print("Email format looks valid")
else:
    print("Invalid email format")