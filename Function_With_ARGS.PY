def add(*args):
    total = 0


    for num in args:
        total+= num

    return total 



print(add(10,20))
print(add(10,20,60,90))