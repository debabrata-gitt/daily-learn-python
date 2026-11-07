from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def calculate(self, a, b):
        pass

class Addition(Calculator):

    def calculate(self, a, b):
        print("Addition:", a + b)

obj = Addition()
obj.calculate(10, 20)