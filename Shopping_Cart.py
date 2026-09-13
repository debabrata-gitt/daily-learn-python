cart = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500,
    "Bottle": 150
}

total = sum(cart.values())

print("Shopping Cart:")
for item, price in cart.items():
    print(item, "₹", price)

print("Total = ₹", total)