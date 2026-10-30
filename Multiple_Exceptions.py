try:
    num = int(input("Enter Number:"))
    result = 100/num
    print(result)

except(ValueError, ZeroDivisionError):
    print("Invalid Iinput or division by Zero") 
