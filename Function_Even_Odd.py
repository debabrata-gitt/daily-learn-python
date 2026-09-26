def count_even_odd(numbers):
    even = 0
    odd = 0

    for i in numbers:
        if i%2 ==0:
            even+= 1

        else:
            odd += 1

    return even , odd 
list = [50,60,80,1,3,7,2,64,85] 

even,odd = count_even_odd(list)

print("Even:", even)
print("Odd:" ,odd )
