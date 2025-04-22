n=int(input("Enter n: "))
r=int(input("Enter r: "))
n1=1
nr=1
r1=1
for i in range(1,n+1):
    n1=n1*i
for j in range(1,n-r+1):
    nr=nr*j
for k in range(1,r+1):
    r1=r1*k

print("nCr= ", n1/(nr*r1))
print("nPr= ",n1/nr)
