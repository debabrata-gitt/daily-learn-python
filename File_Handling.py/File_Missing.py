
try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File does not exist.")
