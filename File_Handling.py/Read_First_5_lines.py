
with open("students.txt", "r") as file:
    for i in range(5):
        line = file.readline()
        if not line:
            break
        print(line.strip())
