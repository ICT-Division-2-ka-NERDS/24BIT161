for i in range(1,31):
    for j in range(1,31):
        for k in range(1,31):
            if i>j and i>k:
                if j>k:
                    if (j**2)+(k**2)==(i**2):
                        print(i,j,k)
           
