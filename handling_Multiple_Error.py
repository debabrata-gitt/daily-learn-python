try:
    a = int(input("Enter a number: "))
    print(100 / a)

except ArithmeticError:
    print("Arithmetic error occurred")