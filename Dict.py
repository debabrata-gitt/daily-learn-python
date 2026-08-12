d={10:100,20:200,30:300,40:400}
print(d[10])


#change the key value:
d={10:100,20:200,30:300,40:400}
d[10]=1000
d[20]=2000
print(d)

#create some values:
d={10:100,20:200,30:300,40:400}
d.update({50:500})
print(d)
#otherwise another method:
d={10:100,20:200,30:300,40:400}
d[50]=500
print(d)

#delete:
d={10:100,20:200,30:300,40:400}
del d[40]
print(d)
