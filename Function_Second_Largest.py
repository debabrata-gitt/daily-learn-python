def second_largest(lst):
    largest = max(lst)
    second = None

    for i in lst:
        if i != largest:
            if second is None or i > second:
                second = i

    return second


numbers = [10, 25, 45, 30, 20]

print("Second largest:", second_largest(numbers))