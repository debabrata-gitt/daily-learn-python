marks = {
    "Math": 85,
    "Physics": 78,
    "Chemistry": 90
}

highest_subject = max(marks, key=marks.get)

print("Highest marks subject:", highest_subject)
print("Marks:", marks[highest_subject])