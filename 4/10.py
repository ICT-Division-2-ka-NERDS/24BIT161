a=int(input("Enter number of fibonnaci numbers to print: "))
p=0
q=1
for i in range(0,a):
    r=p+q
    print(p, end= ' ')
    p=q
    q=r

