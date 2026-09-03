tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 6, 7)

result = ()

for item in tuple1:
    if item not in tuple2:
        result += (item,)

print("Elements present in first tuple but not in second tuple:", result)