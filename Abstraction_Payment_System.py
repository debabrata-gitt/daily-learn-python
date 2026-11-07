from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print("Paid:", amount, "using UPI")

obj = UPI()
obj.pay(500)