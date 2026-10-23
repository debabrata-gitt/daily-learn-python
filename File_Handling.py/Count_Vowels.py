
with open("demo.txt", "r") as file:
    text = file.read().lower()

count = 0
for char in text:
    if char in "aeiou":
        count += 1

print("Total vowels:", count)
