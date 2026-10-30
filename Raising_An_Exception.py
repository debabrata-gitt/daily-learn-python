try:
    age = 15 

    if age < 18:
        raise Exception("not elligible to vote")


except Exception as e:
    print(e)    