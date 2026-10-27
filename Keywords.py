keyword = input("Enter keyword: ").lower()

with open("data.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        if keyword in line.lower():
            print(f"Line {number}: {line.strip()}")