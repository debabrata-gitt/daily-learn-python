inventory = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 10
}

item = input("Enter item: ")

if item in inventory:
    print("Available:", inventory[item])
else:
    print("Item not found")