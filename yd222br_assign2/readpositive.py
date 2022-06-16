def is_positive_and_odd(n):
    if n > 0 and n % 2 != 0:
        return(True)
    return(False)


for i in range (1,6):
    x = int(input("Please enter a positive and odd integer: "))
    y = is_positive_and_odd ( x )
    if y == True:
        print (x)
    else:
        print (y)
