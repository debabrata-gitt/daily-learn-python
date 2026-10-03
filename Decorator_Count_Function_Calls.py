from functools import wraps

def count_calls(func):
    calls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("Call number:", calls)
        return func(*args, **kwargs)

    return wrapper


@count_calls
def hello():
    print("Hello")


hello()
hello()
hello()