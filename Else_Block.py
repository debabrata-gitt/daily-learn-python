try:
    a = 10
    b = 2
    result = a / b

except ZeroDivisionError:
    print("Error occurred")

else:
    print("Result:", result)