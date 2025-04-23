s={'Aashna','Barry','Alicia','Arnold','Akansha','Bert','Bolt','Anika','Basmian'}
a=set()
b=set()
for i in s:
    if i[0]=='A':
        a.update({i})
    else:
        b.update({i})

print('Names with A: ',a)
print('Names with B: ',b)
