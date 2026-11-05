try:
    def show():
        print(x)
        x = 10

    show()

except UnboundLocalError:
    print("Local variable referenced before assignment")