def success():
    print("Operation successful")


def process(callback):
    print("Processing...")
    callback()


process(success)