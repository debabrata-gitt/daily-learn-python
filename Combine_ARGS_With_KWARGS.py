def display (*args,**kwargs):

    print("Arguements:")

    for value in args :
        print (value)


    print("Keywords Arguements:")


    for key, value in kwargs.items():
        print(key,":",value)


display(10,20,50, name="Debabrata", age=20)     
       