from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

class BMW(Car):

    def start(self):
        print("BMW starts with a button")

obj = BMW()
obj.start()