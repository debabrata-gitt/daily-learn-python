try:
    numbers = iter([10, 20, 30])

    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))

except StopIteration:
    print("No more elements available")