with open("data.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("File is empty")