with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

content = content.upper()

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(content)

print(content)