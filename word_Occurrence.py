with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read().lower()

word = input("Enter word: ").lower()
words = content.split()

print("Occurrences:", words.count(word))