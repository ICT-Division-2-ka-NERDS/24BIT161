l=int(input("Enter length of rectangle= "))
b=int(input("Enter breadth of rectangle= "))
if l*b>2*(l+b):
    print("Area is greater than perimeter.")
else:
    print("Perimeter is greater than area.")
