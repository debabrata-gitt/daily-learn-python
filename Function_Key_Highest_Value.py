def highest_subject(data):
    key_name = ""
    maximum = 0

    for key, value in data.items():
        if value > maximum:
            maximum = value
            key_name = key

    return key_name

marks = {
    "Math": 80,
    "English": 70,
    "Python": 90
}

print("Highest subject:", highest_subject(marks))