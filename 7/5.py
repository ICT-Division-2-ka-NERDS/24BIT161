a={'apples':25,'oranges':80,'banana':10,'bread':120,'washcloth':20,'spoon':15,'fork':20}
b={'apples':12,'oranges':6,'banana':5,'bread':2,'washcloth':1,'spoon':8,'fork':8}
bill=0
for i in a:
    for j in b:
        if i==j:
            bill+=a[i]*b[j]


print("Bill= ",bill)
