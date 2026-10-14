class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        bonus = self.basic_salary * 0.10
        return self.basic_salary + bonus

    def display(self):
        print("Employee:", self.name)
        print("Total Salary:", self.calculate_salary())


e = Employee("Amit", 30000)
e.display()