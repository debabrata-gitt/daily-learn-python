class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(self.brand, "-", self.color)


car1 = Car("Toyota", "White")
car2 = Car("BMW", "Black")
car3 = Car("Honda", "Red")

car1.show()
car2.show()
car3.show()