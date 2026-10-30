try:
    print("Try block executed")
    x = 10 / 2

except ZeroDivisionError:
    print("Error occurred")

finally:
    print("Finally block executed")