
with open("demo.txt", "r") as file:
    text = file.read()

with open("reversed.txt", "w") as file:
    file.write(text[::-1])

print("Content reversed!")
