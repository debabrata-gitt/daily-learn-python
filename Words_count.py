with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

print("Total words:", len(words))