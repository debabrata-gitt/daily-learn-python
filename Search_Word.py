with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Python is easy. Python is powerful.")

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

word = input("Enter word to search: ")

if word.lower() in content.lower().split():
    print("Word found!")
else:
    print("Word not found!")