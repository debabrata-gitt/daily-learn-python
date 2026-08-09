n=int(input("Check Your Number Is Prime Or Not."))


count=0

for i in range (1,n+1):
    if n%i==0:
     count= count + 1

print(f": {count}")

if count==2:
   print("Your Number Is Prime.")
else:
   print("Your Number Is Not Prime.")
      