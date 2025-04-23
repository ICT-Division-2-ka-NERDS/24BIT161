a=(1,2,3,4,5)
print(a)
b=int(input("Choose element to modify= "))
x=input("Enter modified element= ")
i=a.index(b)
l=list(a)
l[i]=x
a=tuple(l)
print(a)
