try:
    with open("student.txt", "w") as f:
        f.write("Hello")

except PermissionError:
    print("Permission denied")