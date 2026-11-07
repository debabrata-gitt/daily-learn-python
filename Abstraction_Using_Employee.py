from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):

    def salary(self):
        print("Manager salary: 50000")

obj = Manager()
obj.salary()