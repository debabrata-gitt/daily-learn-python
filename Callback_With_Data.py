def display(result):
    print("Result:", result)


def calculate(a, b, callback):

    result = a + b
    callback(result)


calculate(10, 20, display)