a=int(input("Marks in subject 1= "))
b=int(input("Marks in subject 2= "))
c=int(input("Marks in subject 3= "))
print("Avg marks= ",(a+b+c)/3)
print("Total marks= ", a+b+c)
x=[a,b,c]
fail=0
for j in range(0,3):
    i=x[j]
    if i<=39:
        print("Grade= F in subject",j+1)
        fail=fail+1
    elif i<=44 and i>=40:
        print("Grade= P in subject",j+1)
    elif i<=49 and i>=45:
        print("Grade= C in subject",j+1)
    elif i<=54 and i>=50:
        print("Grade= B in subject",j+1)
    elif i<=59 and i>=55:
        print("Grade= B+ in subject",j+1)
    elif i<=69 and i>=60:
        print("Grade= A in subject",j+1)
    elif i<=79 and i>=70:
        print("Grade= A+ in subject",j+1)
    else:
        print("Grade= O in subject",j+1)

if fail==0:
    print("Student has passed.")
else:
    print("Student has failed.")
