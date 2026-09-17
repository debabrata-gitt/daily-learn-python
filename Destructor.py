class Student:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Object deleted")

s = Student("Rahul")

del s