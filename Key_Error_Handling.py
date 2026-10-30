try:
    student = {"name": "Rahul", "age": 20}
    print(student["marks"])

except KeyError:
    print("Key does not exist")