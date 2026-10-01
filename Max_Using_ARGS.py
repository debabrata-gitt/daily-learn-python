def maximum(*numbers):
    max_value = numbers[0]

    for num in numbers :
        if num > max_value:
            max_value = num 


    return max_value

print(maximum(10,20,60,80,20,70))        