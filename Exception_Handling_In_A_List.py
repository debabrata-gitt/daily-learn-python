try:
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    print(numbers[index])

except ValueError:
    print("Enter an integer")

except IndexError:
    print("Invalid list index")