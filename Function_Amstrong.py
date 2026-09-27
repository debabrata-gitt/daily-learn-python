def armstrong(n):
    original = n
    total = 0
    digits = len(str(n))

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original

n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong")