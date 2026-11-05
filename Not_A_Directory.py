try:
    import os
    os.listdir("student.txt")

except NotADirectoryError:
    print("The given path is not a directory")