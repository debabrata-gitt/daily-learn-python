import json
from pathlib import Path

path = Path("students.json")

if path.exists():
    try:
        with open(path, "r", encoding="utf-8") as file:
            students = json.load(file)

        if not isinstance(students, list):
            raise ValueError("Expected a list of students.")

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        raise SystemExit

else:
    students = []

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

students.append({"name": name, "marks": marks})

with open(path, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("New student added successfully!")