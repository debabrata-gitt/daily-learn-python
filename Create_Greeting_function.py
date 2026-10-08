def greeting(message):

    def greet(name):
        return message + " " + name

    return greet


hello = greeting("Hello")
good_morning = greeting("Good Morning")

print(hello("Debabrata"))
print(good_morning("Debabrata"))