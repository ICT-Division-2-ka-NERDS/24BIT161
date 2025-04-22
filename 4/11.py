a=float(input("Enter angle for sin(x) in degrees= "))
n=int(input("Up to how many terms= "))
x=a*3.14159/180
sinx=0
for i in range(n):
    fact=1
    power=(2*i)+1
    sign=(-1)**i
    for j in range(1, power+1):
        fact=fact*j
    sinx+=(sign*(x**power))/fact
    

print('value of sin(x)= ',sinx)
