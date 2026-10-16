with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("notes.txt", "w", encoding="utf-8") as file:
    for number, line in enumerate(lines, start=1):
        file.write(f"{number}. {line}")

print("Line numbers added!")