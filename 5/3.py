import random
a=[random.randint(1,31) for i in range(50)]
print(a)
b=[]
for i in range(0,50):
    if a[i] in b:
        continue
    else:
        b.append(a[i])
print("Duplicates removed: ",b)
