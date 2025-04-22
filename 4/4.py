a=int(input("Enter a number: "))
prime=0
s=1
arm=0
x=str(a)
pali=''
for i in range(2,a):
    if a%i==0:
        prime=prime+1
        s=s+i
if prime==0:
    print("Number is prime.")
else:
    print("Number is not prime.")

if s==a:
    print("Number is perfect.")
else:
    print("Number is not perfect.")
    
t=a
for i in range(0,len(x)):
    b=t//10
    c=t-(b*10)
    t=b
    arm=arm+(c**3)
if arm==a:
    print("Number is armstrong.")
else:
    print("Number is not armstrong.")

for i in range(len(x)-1,-1,-1):
    pali=pali+x[i]
if pali==x:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")

if (a**2)%(10**len(x))==a:
    print("Number is automorphic.")
else:
    print("Number is not automorphic.")
    

    
