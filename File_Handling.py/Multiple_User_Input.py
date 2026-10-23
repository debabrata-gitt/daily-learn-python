
with open("details.txt", "w") as file:
    for i in range(3):
        name = input("Enter name: ")
        file.write(name + "\n")

print("All names saved!")
