def information(**kwargs):
    print("Your Information Is \n")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")
information(name="Debabrata",age=19,designation="ai/ml")
