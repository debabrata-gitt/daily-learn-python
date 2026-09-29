def square(n):
    return n * n

def calculate(func, value):
    return func(value)

result = calculate(square, 5)

print(result)