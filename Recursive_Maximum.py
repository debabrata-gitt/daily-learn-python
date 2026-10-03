def maximum(lst):
    if len(lst) == 1:
        return lst[0]

    max_rest = maximum(lst[1:])

    if lst[0] > max_rest:
        return lst[0]

    return max_rest


print(maximum([10, 45, 23, 80, 12]))