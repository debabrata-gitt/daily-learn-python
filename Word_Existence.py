text = input("Enter a sentence: ")
word = input("Enter word to search: ")

if word in text:
    print("Word found")
else:
    print("Word not found")