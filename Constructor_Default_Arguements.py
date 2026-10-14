class Product:
    def __init__(self, name, price=100):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, self.price)


p1 = Product("Pen")
p2 = Product("Book", 250)

p1.display()
p2.display()