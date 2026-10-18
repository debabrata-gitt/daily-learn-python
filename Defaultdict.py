from collections import defaultdict

students = [
    ("Rahul", "CSE"),
    ("Debabrata", "AIML"),
    ("Satak", "CSE"),
    ("Amit", "AIML")
]

groups = defaultdict(list)

for name, department in students:
    groups[department].append(name)

for department, names in groups.items():
    print(department, ":", names)