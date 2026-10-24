
old_word = input("Word to replace: ")
new_word = input("New word: ")

with open("demo.txt", "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open("demo.txt", "w") as file:
    file.write(text)

print("Word replaced!")
