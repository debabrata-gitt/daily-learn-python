
with open("fruits.txt", "r") as file:
    fruits = [line.strip() for line in file]

print(fruits)
print("Total fruits:", len(fruits))
