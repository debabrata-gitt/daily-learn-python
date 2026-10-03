def product (lst):
    if len(lst)==0:
        return 1

    return lst [0] * product(lst[1:])

print(product([1,2,3,4,5,6]))
