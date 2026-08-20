from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")


def createfile():
    try:
        readfileandfolder()

        name = input("Please tell your file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file? ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists.")

    except Exception as err:
        print(f"An error occurred: {err}")

def readfile():
     try:
         readfileandfolder()
         name = input("which file you want to read .")
         p= Path(name) 
         if p.exists() and p.is_file():
             with open(p,"r")as fs:
                  data=fs.read()
                  print(data)         
             print("Readed successfully.")
         else:
             print("The file does not exist.")
     except Exception as err:
         print(f"an error occurred as {err}")



def updatefile():
    try:
        readfileandfolder()
        name=input("Tell Which File Do You Want To Update.")
        p=Path(name)
        if p.exists() and p.is_file():
          print("Press 1 for changing the name of your file .")
          print("Press 1 for overwriting the name of your file .")
          print("Press 1 for appending some content your file .")

        res=int(input("tell your response."))

        if res==1:
            name2=input("Tell Your New File Name")
            p2=Path(name2)
            p.rename(p2)

        if res==2:
            with open (p,"w") as fs:
                data=input("Tell what you want to overwrite.")
                fs.write(data)

        if res==3:
          with open(p,"a")as fs:
              data=input("Tell what you want to append.")
              fs.write(" "+data)

    except Exception as err: 
        print(f"an error occurred as {err}")  




def deletefile():
    try:


        readfileandfolder()
        name=input("Which file you want to delete?")
        p= Path(name)

        if p.exists() and p.is_file():
         os.remove(p) 

         print("File removes successfully.")

        else:
            print("No Such File Exist.")

    except Exception as err:
        print(f"an error occurred as {err}")        


                 



        print("Press 1 for creating a file")
        print("Press 2 for reading a file")
        print("Press 3 for updating a file")
        print("Press 4 for deleting a file")

check = int(input("Please tell your response: "))

if check == 1:
    createfile()

if check == 2:
    readfile()    

if check==3:
    updatefile()


if check==4:
    deletefile()    