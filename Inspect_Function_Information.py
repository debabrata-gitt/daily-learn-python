import inspect

def greet(name, age=18):
    return f"{name} is {age} years old"


print(inspect.signature(greet))
print(inspect.getdoc(greet))