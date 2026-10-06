def binary_search(lst, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid

    elif target < lst[mid]:
        return binary_search(lst, target, low, mid - 1)

    else:
        return binary_search(lst, target, mid + 1, high)


numbers = [10, 20, 30, 40, 50, 60, 70]

result = binary_search(numbers, 50, 0, len(numbers) - 1)

print("Index:", result)