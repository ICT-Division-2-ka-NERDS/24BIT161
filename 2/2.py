a=int(input("Enter first value= "))
b=int(input("Enter second value= "))
c=int(input("Enter third value= "))
if a>b and a>c:
    print(a, " is the largest value.")
    if b>c:
        print(c, " is the smallest value.")
    else:
        print(b, " is the smallest value.")
elif b>c and b>a:
    print(b, " is the largest value.")
    if a>c:
      print(c, " is the smallest value.")
    else:
      print(a, " is the smallest value.")
else:
    print(c, " is the largest value.")
    if a>b:
      print(b, " is the smallest value.")
    else:
      print(a, " is the smallest value.")
