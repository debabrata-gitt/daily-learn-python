numbers = ()

for i in range(10):
    num = int(input(f"Enter element {i + 1}: "))
    numbers += (num,)

result = ()

for num in numbers:
    if num < 0:
        result += (0,)
    else:
        result += (num,)

print("Original tuple:", numbers)
print("New tuple:", result)