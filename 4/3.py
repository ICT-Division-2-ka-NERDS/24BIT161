a=input("Enter a string: ")
dig=0
alp=0
for i in a:
    if i.isdigit()==True:
        dig=dig+1
    elif i.isalpha()==True:
        alp=alp+1
print("No. of alphabets= ",alp, 'and no. of digits= ', dig)
