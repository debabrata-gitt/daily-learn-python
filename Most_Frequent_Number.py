t = tuple(map(int, input("Enter Elements : ").split()))
most = t[0]

for i in t :
    if t.count(i) > t.count(most):
        most = i

print("Most frequent  number is : ", most)