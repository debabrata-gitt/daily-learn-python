text = input("Enter a sentence: ")

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

result = text.replace(old_word, new_word)

print("Updated sentence:", result)