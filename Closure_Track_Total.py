def tracker():

    total = 0

    def add(value):

        nonlocal total
        total += value

        return total

    return add


track = tracker()

print(track(10))
print(track(20))
print(track(30))