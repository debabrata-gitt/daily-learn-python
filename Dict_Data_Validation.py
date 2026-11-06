try:
    student = {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    }

    print("Name:", student["name"])
    print("Marks:", student["score"])

except KeyError:
    print("Student data not found")