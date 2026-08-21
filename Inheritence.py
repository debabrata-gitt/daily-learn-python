class Factorymumbai:
    a="Iam an attribute mentioned inside the factory." 
    def hello(self):
        print("hello i am a method mentioned inside factory.")

class Factorypune(Factorymumbai):
    pass


obj=Factorymumbai()


obj2=Factorypune()


print(obj2.hello())

