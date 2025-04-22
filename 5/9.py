l1=[1,2,3,4,5,6,7,8,9]
l2=[2,5,6,8,0,15,34]
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)

print(l3)
