student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

with open("student.txt", "w") as file:
    for key, value in student.items():
        file.write(f"{key}: {value}\n")

print("Student data saved successfully!")