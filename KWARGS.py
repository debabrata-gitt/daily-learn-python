def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Rahul", age=20, marks=85)