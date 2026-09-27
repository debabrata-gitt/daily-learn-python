def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def strong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += factorial(digit)
        n //= 10

    return total == original


n = int(input("Enter number: "))

if strong(n):
    print("Strong Number")
else:
    print("Not Strong")