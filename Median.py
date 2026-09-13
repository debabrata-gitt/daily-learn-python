l=list(map(int,input("enter elements :").split()))
l.sort()
n=len(l)

if n%2==1:
  median =l[n//2]
else:
  median= l[n//2-1]

print("median=",median)