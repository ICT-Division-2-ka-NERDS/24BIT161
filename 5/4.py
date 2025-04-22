import random
a=[random.randint(-100,100) for x in range(30)]
print(a)
p=[]
n=[]
for i in a:
    if i<0:
        n.append(i)
    else:
        p.append(i)

print("Positive list: ",p)
print("Negative list: ",n)
