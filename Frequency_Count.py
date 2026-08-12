a=[50,60,50,80,60,50,40,60,40,80]
d={}
for i in a :
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
    print(d)    