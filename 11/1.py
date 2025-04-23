def isint():
    
    while True:
        try:
            a = int(input("Enter an integer: "))
            print("Integer= ",a)
            break
        except ValueError:
            print("Error:Entered value is not integer. Try again.")

isint()
