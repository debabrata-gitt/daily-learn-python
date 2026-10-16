with open("data.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

if words:
    shortest = min(words, key=len)
    print("Shortest word:", shortest)
else:
    print("File is empty")