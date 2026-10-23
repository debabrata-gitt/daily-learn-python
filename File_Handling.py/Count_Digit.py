
with open("demo.txt", "r") as file:
    text = file.read()

count = sum(char.isdigit() for char in text)
print("Total digits:", count)
