import csv

students = [
    ["Name", "Marks"],
    ["Rahul", 80],
    ["Debabrata", 90],
    ["Satak", 75]
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created!")