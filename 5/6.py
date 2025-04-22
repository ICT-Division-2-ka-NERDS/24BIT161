n=int(input("Enter number of elements in list: "))
l1=[]
for i in range(0,n):
    t=int(input("Enter temperature in Fahrenheit: "))
    l1.append(t)
print(l1)
for i in range(0,n):
    l1[i]=(l1[i]-32)*5/9

print(l1)
