import csv

search_name = input("Enter student name: ").strip().lower()
found = False

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for student in reader:
        if student["Name"].lower() == search_name:
            print("Student found!")
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Marks:", student["Marks"])
            found = True
            break

if not found:
    print("Student not found!")