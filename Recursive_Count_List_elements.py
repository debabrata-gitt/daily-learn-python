def count_elements (lst):
    if lst ==[]:
        return 0


    return 1 + count_elements(lst[1:])


print(count_elements([10,20,30,40,60,80]))
