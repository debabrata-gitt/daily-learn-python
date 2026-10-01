def maximum(t):
    max_value = t[0]

    for i in t:
        if i > max_value:
            max_value = i

    return max_value

numbers = (10, 50, 20, 40)

print("Maximum:", maximum(numbers))