
word = input("Enter word: ").lower()

with open("demo.txt", "r") as file:
    words = file.read().lower().split()

print("Occurrences:", words.count(word))
