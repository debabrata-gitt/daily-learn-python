dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 50,
    "c": 60,
    "d": 70
}

common = {}

for key in dict1:
    if key in dict2:
        common[key] = dict1[key]

print(common)