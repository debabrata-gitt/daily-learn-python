class MyError(Exception):
    pass


try:
    raise MyError("This Is A Custom Exception")

except MyError as e:
    print(e)