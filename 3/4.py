a= input("Enter the first string: ")
b= input("Enter the second string: ")
if b in a:
    a=a.replace(b,'')
    print(a)
else:
    print(b, "is not there in", a)
