s=input("Enter string: ")
a=list(s.lower())
v=0
for i in range(0,len(a)):
  x=a[i]
  if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
    v=v+1
print("No. of vowels in string= ",v)
