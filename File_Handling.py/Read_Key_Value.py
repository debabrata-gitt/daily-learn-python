student = {}

with open("student.txt", "r") as file:
    for line in file:
        key, value = line.strip().split(": ", 1)
        student[key] = value

print(student)