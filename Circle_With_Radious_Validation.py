class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


c = Circle(7)
print("Area:", round(c.area(), 2))