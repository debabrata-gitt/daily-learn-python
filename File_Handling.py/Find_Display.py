with open("data.txt", "r") as file:
    lines = file.readlines()

limit = 50

for number, line in enumerate(lines, start=1):
    if len(line.rstrip("\n")) > limit:
        print(f"Line {number}: {line.rstrip()}")

print("Search completed!")