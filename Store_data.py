import json

student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "marks": float(input("Enter marks: "))
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully!")