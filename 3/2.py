a=input("Enter a string: ")
b=''
c=''
d=''
for i in range(0,len(a)):
    if ord(a[i])>=65 and ord(a[i])<=90:
        x=chr(ord(a[i])+32)
        b=b+x
    else:
        b=b+a[i]
    
print("ALL LOWERCASE= ",b)

for i in range(0,len(a)):
    if ord(a[i])>=97 and ord(a[i])<=122:
        x=chr(ord(a[i])-32)
        c=c+x
    else:
        c=c+a[i]

print("ALL UPPERCASE= ",c)

for i in range(0,len(a)):
    if i%2==0:
        if ord(a[i])>=65 and ord(a[i])<=90:
            x=chr(ord(a[i])+32)
            d=d+x
        else:
            d=d+a[i]
    else:
        if ord(a[i])>=97 and ord(a[i])<=122:
            x=chr(ord(a[i])-32)
            d=d+x
        else:
            d=d+a[i]

print("TOGGLECASE= ",d)



