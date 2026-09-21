n = input("Enter number: ")

largest = 0

for digit in n:
    if int(digit) > largest:
        largest = int(digit)

print("Largest digit:", largest)