def outer(x):

    def square():
        return x * x

    return square()

print(outer(5))