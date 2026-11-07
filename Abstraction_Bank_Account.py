from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest(self):
        pass

class SBI(Bank):

    def interest(self):
        print("SBI interest rate is 7%")

obj = SBI()
obj.interest()