numbers = list(map(int, input("Enter numbers: ").split()))

positive = []
negative = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)