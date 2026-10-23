
word = input("Enter word to search: ")

with open("demo.txt", "r") as file:
    text = file.read()

if word.lower() in text.lower():
    print("Word found!")
else:
    print("Word not found!")
