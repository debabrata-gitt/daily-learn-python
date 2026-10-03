from functools import wraps

def show_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@show_name
def greet():
    print("Hello Python")


greet()