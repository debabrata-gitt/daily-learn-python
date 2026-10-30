try:
    print("Outer try block")

    try:
        a = 10/0

    except ZeroDivisionError:
        print("Inner exception handled") 

except Exception:
    print("Outer Exception handled ")           