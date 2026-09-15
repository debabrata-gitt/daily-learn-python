numbers = [2, 5, 2, 8, 2, 9, 2]

search = int(input("Enter number: "))
count = 0

for n in numbers:
    if n == search:
        count += 1

print("Found", count, "times")