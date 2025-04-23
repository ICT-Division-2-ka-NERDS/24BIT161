def length(s):
    print(len(s))
    if len(s)>8:
        return True
    else:
        return False

l=['Shashi','Gaurshankar','Mitradas','Kalampurva','Ankit','Parulyathi']
l2=list(filter(length,l))
print(l)
print(l2)
