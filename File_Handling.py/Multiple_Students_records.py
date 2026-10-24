
with open("students.txt", "w") as file:
    n = int(input("How many students? "))

    for i in range(n):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        file.write(f"{name}, {marks}\n")

print("All records saved!")
