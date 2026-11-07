from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        r = 5
        print("Area:", 3.14 * r * r)

obj = Circle()
obj.area()