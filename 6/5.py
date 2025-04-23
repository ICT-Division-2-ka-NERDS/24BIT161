a=[(1,2),(),(5,),(4,5),(),(),(9,),(1,2,3),(),(6,),() ]
b=[]
print(a)
for i in a:
    if not i:
        print('removed')
    else:
        b.append(i)
print(b)
