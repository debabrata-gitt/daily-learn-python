
fruits = ["Apple", "Mango", "Banana", "Orange"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

print("Fruit list saved!")
