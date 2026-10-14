class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)


s1 = Student("Rahul", 101, 85)
s1.display()