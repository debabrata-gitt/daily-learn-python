with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

if lines:
    longest = max(lines, key=len)

    print("Longest line:")
    print(longest.strip())
    print("Characters:", len(longest.rstrip("\n")))
else:
    print("File is empty.")