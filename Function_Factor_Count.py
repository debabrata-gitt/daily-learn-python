def count_factors(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return count

n = int(input("Enter number: "))

print("Factors:", count_factors(n))