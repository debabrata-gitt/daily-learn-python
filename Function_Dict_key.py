def search_key(data, key):
    if key in data:
        return True
    return False

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

key = input("Enter key: ")

if search_key(student, key):
    print("Key Found")
else:
    print("Key Not Found")