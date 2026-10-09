def add_result(result):
    print("Addition:", result)


def multiply_result(result):
    print("Multiplication:", result)


def calculate(a, b, operation, callback):

    result = operation(a, b)

    callback(result)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


calculate(10, 20, add, add_result)
calculate(10, 20, multiply, multiply_result)