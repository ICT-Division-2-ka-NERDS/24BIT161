a=set()
for i in range(0,5):
    n=input("Enter name: ")
    a.update({n})
print(a)
l=list(a)
r=input("enter name u want to replace: ")
rr=input("replaced name: ")
x=l.index(r)
l[x]=rr
a=set(l)
print(a)
for i in range(0,2):
    n=input("Name to delete= ")
    a.discard(n)
print(a)
