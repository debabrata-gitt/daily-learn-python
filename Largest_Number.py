l=[50,78,94,658,784,1025]

largest =l[0]
index=0
for i in range(len(l)):
  if l[i]>largest:
        largest=l[i]
        index=i
print(f"Your Largest Number Is {largest} And Its Index Is {index}")        