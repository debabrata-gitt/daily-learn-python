a=input("Enter Your String Name Here To Check Palindrome.")
b=""
for i in range (len(a)-1,-1,-1,):
    b=b+a[i]

if b==a:
  print("Your String Is Palindrome.")
else:
  print("Your String Is Not Palindrome.")  
