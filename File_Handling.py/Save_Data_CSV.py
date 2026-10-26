import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Rahul", 20, 85])
    writer.writerow(["Amit", 19, 90])
    writer.writerow(["Priya", 21, 88])

print("CSV file created successfully!")