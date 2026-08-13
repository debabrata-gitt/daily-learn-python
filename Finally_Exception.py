a=int(input("Tell Your Number ."))
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")

else :
    print("Good There Is No Exception.")

    
finally:
    print("I Will Run No Matter What.") 


print("okay i have done the division .")