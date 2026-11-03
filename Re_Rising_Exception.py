try:
    try:
        x = 10 / 0

    except ZeroDivisionError:
        print("Error caught")
        raise

except ZeroDivisionError:
    print("Error raised again")