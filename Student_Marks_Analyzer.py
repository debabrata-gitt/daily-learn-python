marks = {
    "Rahul": 96,
    "Amit": 92,
    "Priya": 85,
    "Riya": 67
}

topper = max(marks, key=marks.get)

print("Topper:", topper)
print("Marks:", marks[topper])