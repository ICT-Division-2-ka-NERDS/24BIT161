import random
a=[random.randint(1,100) for x in range(20)]
print('list= ',a)
b=int(input("Enter number to find position(s): "))
for i in range(0,len(a)):
    if a[i]==b:
        print(b, "is present at the", i+1,'th position and index is', i)
        
