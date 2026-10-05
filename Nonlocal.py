def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5

    inner()
    print(x)


outer()