users = {
    "admin": "1234",
    "rahul": "5678"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username] == password:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Username not found")