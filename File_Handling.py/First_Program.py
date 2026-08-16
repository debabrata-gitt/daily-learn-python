from pathlib import Path

def readfileandfolder():
    path=path('')
    items=list(path.rglob('*'))
    for i , items in enumerate(items):
       print(f"{i+1} : {items}")




def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name")
        p = Path(name)
        
        if not p.exists():
            with open (p,"w")as fs:
                data=input("What you want to write in this file")
                fs.write(data)

            print (F"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exist.")
    except Exception as err:
            print(f"an error occurredas{err}")        






print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check=int(input("please tell your response."))
if check == 1 :
    createfile()