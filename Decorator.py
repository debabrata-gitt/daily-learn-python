class Animal:
    @property
    def show(self):
        print("hello how are you.")



obj =Animal()
obj.show        



def decorate(func):
    def wrapper():
        print("i will print myself before function.")
        func()
        print("i will print after the function.")
    return wrapper


@decorate
def hello():
    print("I am Debabrata")

hello()