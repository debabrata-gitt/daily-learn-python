def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def multiple_gcd(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return gcd(numbers[0], multiple_gcd(numbers[1:]))


numbers = [48, 72, 120]

print(multiple_gcd(numbers))