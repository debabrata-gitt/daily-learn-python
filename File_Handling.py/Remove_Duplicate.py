with open("data.txt", "r") as file:
    lines = file.readlines()

unique_lines = list(dict.fromkeys(lines))

with open("data.txt", "w") as file:
    file.writelines(unique_lines)

print("Duplicate lines removed!")