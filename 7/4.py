a=input("Enter a string: ")
d={}
for i in a:
    x=i
    y=a.count(i)
    d.update({x:y})

print(d)
