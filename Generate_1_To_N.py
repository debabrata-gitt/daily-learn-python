def generate(n):
    for i in range(1, n + 1):
        yield i


for value in generate(5):
    print(value)