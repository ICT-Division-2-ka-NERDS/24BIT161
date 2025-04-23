a={123:[21,200000],193:[23,120000],147:[21,150000],161:[21,500000],95:[21,290000],129:[25,130000],190:[23,450000],145:[21,34000],183:[25,270000],111:[23,370000]}
print(a)
s=[]
for i in a:
    if a[i][0] not in s:
        s.append(a[i][0])
for j in s:
    dep=[]
    for k in a:
        if j==a[k][0]:
            dep.append(a[k][1])
        
    print("for department", j, 'minimum salary= ', min(dep), ' and maximum salary= ', max(dep))
            
