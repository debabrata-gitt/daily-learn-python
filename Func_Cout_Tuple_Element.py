def count_element(t, value):
    count = 0

    for i in t:
        if i == value:
            count += 1

    return count

numbers = (1, 2, 2, 3, 2, 4)

print(count_element(numbers, 2))