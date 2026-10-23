
with open("demo.txt", "r") as file:
    text = file.read()

words = text.split()
print("Total words:", len(words))
