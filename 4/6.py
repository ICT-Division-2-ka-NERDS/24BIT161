for i in range(0,24):
    if i>=0 and i<=5:
        print(i,'midnight')
    elif i>=6 and i<=11:
        print(i, 'AM')
    elif i>=12 and i<=17:
        if i>12:
            print(i-12, 'noon')
        else:
            print(i, 'noon')
    elif i>=18 and i<=23:
        print(i-12, 'PM')
    
