students = [
    {"name": "Rahul", "marks": 75},
    {"name": "Amit", "marks": 90},
    {"name": "Riya", "marks": 82}
]


def get_marks(student):
    return student["marks"]


result = sorted(students, key=get_marks, reverse=True)

for student in result:
    print(student["name"], student["marks"])