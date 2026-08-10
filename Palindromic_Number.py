a=int(input("Tell Your Number."))
copy=a
rev=0
while a>0:
    rev=rev*10+a%10
    a=a//10
    print(rev)
    if copy==rev:
        print("Palindromic Number.")
    else:
        print("Its Not A Palindromic Number.")