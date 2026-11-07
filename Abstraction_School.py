from abc import ABC, abstractmethod

class School(ABC):

    @abstractmethod
    def study(self):
        pass

class Student(School):

    def study(self):
        print("Student is studying Python")

obj = Student()
obj.study()