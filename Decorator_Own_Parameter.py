from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print("Hello", name)


greet("Rahul")