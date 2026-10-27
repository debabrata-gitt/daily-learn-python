with open("data.txt", "r") as file:
    lines = file.readlines()

lines.sort(key=str.lower)

with open("sorted.txt", "w") as file:
    file.writelines(lines)

print("Lines sorted!")