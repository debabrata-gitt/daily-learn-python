with open("data.txt", "r") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Total lines:", len(lines))
print("Total words:", len(words))
print("Total characters:", characters)