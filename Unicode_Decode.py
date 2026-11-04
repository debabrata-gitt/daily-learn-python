try:
    with open("data.txt", "rb") as file:
        data = file.read()

    print(data.decode("utf-8"))

except UnicodeDecodeError:
    print("Unable to decode the file")