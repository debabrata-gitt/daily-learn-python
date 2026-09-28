def search(lst, value):
    for i in lst:
        if i == value:
            return True

    return False


numbers = [10, 20, 30, 40]

n = int(input("Enter number to search: "))

if search(numbers, n):
    print("Found")
else:
    print("Not Found")