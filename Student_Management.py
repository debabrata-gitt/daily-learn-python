students = {}

while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student added!")

    elif choice == "2":

        if not students:
            print("No students found.")

        else:
            for roll, student in students.items():
                print("\nRoll:", roll)
                print("Name:", student["name"])
                print("Marks:", student["marks"])

    elif choice == "3":

        roll = input("Enter Roll Number: ")

        if roll in students:
            student = students[roll]

            print("Name:", student["name"])
            print("Marks:", student["marks"])
        else:
            print("Student not found.")

    elif choice == "4":

        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Student deleted!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")