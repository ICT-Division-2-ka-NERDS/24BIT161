import random
a=random.sample(range(15,46),10)
s=set(a)
print(s)
p=[]
count=0
for i in s:
    if i<30:
        count+=1
    elif i>35:
        p.append(i)

for j in p:
    s.discard(j)

print("Under 30= ",count)
print("new set= ",s)
