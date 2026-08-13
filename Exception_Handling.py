a=int(input("Tell Your Number ."))
try:
    print(10/a)
except ZeroDivisionError:
    print("Sorry You can Not Divide By Zero.")

print("I Have Done The Division Completely.")   



a=int(input("Tell Your Number ."))
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")

print("okay i have done the division .")
    