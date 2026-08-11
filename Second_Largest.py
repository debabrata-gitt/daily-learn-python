l=[10,53,67,844,420]
largest=l[0]
second_largest=l[0]

for i in l:
    if i>largest:
        second_largest=largest
        largest=i
    elif i >second_largest:
        second_largest=i

            
print(f" Your largest Number Is {largest} And Your Second Largest Number Is {second_largest}")        