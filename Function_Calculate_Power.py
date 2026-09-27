def power(a, b):
    result = 1

    for i in range(b):
        result = result * a

    return result

a = int(input("Enter base: "))
b = int(input("Enter power: "))

print("Result:", power(a, b))