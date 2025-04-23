def palidrome():
    
    lst = ['madam','Python',"malayalam",12321]
    def isPalindrome(s):
        if(type(s)==str):
            x=s
        else:
            x=str(s)
        if(x[::-1]==x[::]):
            return True
        else:
            return False
        
    l=list(filter(isPalindrome,lst))
    print(l)
    
palidrome()
