def double_result(func):

    def wrapper(*args):
        result = func(*args)
        return result * 2

    return wrapper


@double_result
def add(a, b):
    return a + b


print(add(10, 20))