with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nLearning Python every day.")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())