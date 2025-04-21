a=int(input("Enter x coordinate of centre= "))
b=int(input("Enter y coordinate of centre= "))
r=int(input("Enter radius= "))
p=int(input("Enter x coordinate of point= "))
q=int(input("Enter y coordinate of point= "))
if pow((p-a),2)+pow((q-b),2)<r**2:
    print("Point lies inside circle")
elif pow((p-a),2)+pow((q-b),2)==r**2:
    print("Point lies on circle")
else:
    print("Point lies outside circle")
