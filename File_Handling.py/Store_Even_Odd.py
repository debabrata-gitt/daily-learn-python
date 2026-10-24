
numbers = [12, 7, 24, 9, 16, 3, 10]

with open("even.txt", "w") as even_file, \
     open("odd.txt", "w") as odd_file:

    for number in numbers:
        if number % 2 == 0:
            even_file.write(f"{number}\n")
        else:
            odd_file.write(f"{number}\n")

print("Even and odd numbers saved separately!")
