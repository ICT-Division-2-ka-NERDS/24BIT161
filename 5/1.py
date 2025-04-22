import random
a=random.sample(range(1, 100, 2), 5)
print('list1= ',a)
b=random.sample(range(2,100, 2), 4)
print('list2= ',b)

a[2]=b

print('editted list= ',a)

flat=[]
for i in a:
    if type(i)==list:
        flat.extend(i)
    else:
        flat.append(i)

print("flattened list= ",flat)

flat.sort()

print("sorted list= ",flat)
