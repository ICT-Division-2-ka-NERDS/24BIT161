a=('Mira','Sneha',('Vipul',),'Surbhi',('Prithvi',))
girls=0
boys=0
for i in a:
    if isinstance(i,tuple):
        boys+=1
    else:
        girls+=1

print("Number of boys= ",boys)
print("Number of girls= ",girls)
