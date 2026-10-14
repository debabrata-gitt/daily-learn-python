with open("notes.txt", "r", encoding="utf-8") as file:
    for i in range(3):
        line = file.readline()

        if not line:
            break

        print(line.strip())