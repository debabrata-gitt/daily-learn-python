def decimal_to_binary(n):

    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)


n = int(input("Enter number: "))

if n == 0:
    print("0")
else:
    print(decimal_to_binary(n))