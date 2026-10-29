import csv

employees = [
    {"name": "Rahul", "salary": 25000},
    {"name": "Priya", "salary": 32000},
    {"name": "Amit", "salary": 28000}
]

with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    fields = ["name", "salary"]

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(employees)

print("Employee records saved!")