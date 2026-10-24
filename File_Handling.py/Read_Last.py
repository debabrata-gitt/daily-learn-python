
with open("students.txt", "r") as file:
    lines = file.readlines()

if lines:
    print("Last line:", lines[-1].strip())
else:
    print("File is empty.")
