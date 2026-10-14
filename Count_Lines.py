with open("notes.txt", "r", encoding="utf-8") as file:
    line_count = sum(1 for line in file)

print("Total lines:", line_count)