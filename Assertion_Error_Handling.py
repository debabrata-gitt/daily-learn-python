try:
    age=15
    assert age >=18,"Age Must Be 18 or Above ."
    print("Eligible")


except AssertionError as e :
    print(e) 
       