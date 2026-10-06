def even_only(func):

    def wrapper(n):

        if n % 2 != 0:
            print("Only even numbers allowed")
            return

        return func(n)

    return wrapper


@even_only
def square(n):
    return n * n


print(square(10))
print(square(7))