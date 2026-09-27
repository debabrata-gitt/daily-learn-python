def absolute(n):
    if n < 0:
        return -n
    return n

n = int(input("Enter number: "))
print("Absolute:", absolute(n))