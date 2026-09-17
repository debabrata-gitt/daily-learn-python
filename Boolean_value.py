class Student:
    def __init__(self, marks):
        self.marks = marks

    def __bool__(self):
        return self.marks >= 40

s1 = Student(80)
s2 = Student(30)

print(bool(s1))
print(bool(s2))