a="seugdj3740@#%#^ugfh"
char=0
dig=0
spchr=0

for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1    
    else:
        spchr+=1
print(f"your digits are {dig}\nyour alphabets are{char}\nyour special characters are {spchr}")           