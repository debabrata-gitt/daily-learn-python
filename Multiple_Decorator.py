def first(func):

    def wrapper():
        print("First decorator")
        func()

    return wrapper


def second(func):

    def wrapper():
        print("Second decorator")
        func()

    return wrapper


@first
@second
def hello():
    print("Hello Python")


hello()