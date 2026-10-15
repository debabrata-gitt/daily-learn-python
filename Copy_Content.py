with open("source.txt", "w", encoding="utf-8") as file:
    file.write("Python File Handling\n")
    file.write("Learning Python is fun.")

with open("source.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("destination.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("File copied successfully!")