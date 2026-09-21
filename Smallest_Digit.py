n = input("Enter number: ")

smallest = 9

for digit in n:
    if int(digit) < smallest:
        smallest = int(digit)

print("Smallest digit:", smallest)