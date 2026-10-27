with open("data.txt", "r") as file:
    lines = file.readlines()

with open("reversed.txt", "w") as file:
    for line in lines:
        file.write(line.rstrip("\n")[::-1] + "\n")

print("Each line reversed!")