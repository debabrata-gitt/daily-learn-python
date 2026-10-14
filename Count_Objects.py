class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


s1 = Student("Rahul")
s2 = Student("Amit")
s3 = Student("Priya")

print("Total students:", Student.count)