
search_name = input("Enter name to search: ").lower()

with open("students.txt", "r") as file:
    found = False

    for line in file:
        if line.split(",")[0].strip().lower() == search_name:
            print("Record found:", line.strip())
            found = True

if not found:
    print("Student not found.")
