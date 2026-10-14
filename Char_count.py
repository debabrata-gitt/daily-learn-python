with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Characters including spaces:", len(text))
print("Characters excluding whitespace:", sum(not c.isspace() for c in text))