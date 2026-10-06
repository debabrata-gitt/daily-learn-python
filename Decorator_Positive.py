def positive_only(func):

    def wrapper(n):

        if n < 0:
            print("Negative number is not allowed")
            return

        return func(n)

    return wrapper


@positive_only
def square(n):
    return n * n


print(square(5))
print(square(-5))