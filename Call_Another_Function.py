def square(n):
    return n * n

def cube(n):
    return square(n) * n

n = int(input("Enter number: "))

print("Cube:", cube(n))