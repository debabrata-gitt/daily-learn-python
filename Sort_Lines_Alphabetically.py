with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Mango\nApple\nOrange\nBanana\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines.sort(key=str.lower)

with open("sorted.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("Lines sorted successfully!")

with open("sorted.txt", "r", encoding="utf-8") as file:
    print(file.read())