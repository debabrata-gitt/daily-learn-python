from abc import ABC, abstractmethod

class Mobile(ABC):

    @abstractmethod
    def call(self):
        pass

class Samsung(Mobile):

    def call(self):
        print("Calling from Samsung mobile")

obj = Samsung()
obj.call()