with open("data.txt", "r") as file:
    words = file.read().split()

letter = input("Enter starting letter: ").lower()

for word in words:
    if word.lower().startswith(letter):
        print(word)