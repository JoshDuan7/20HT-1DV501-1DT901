repeat = True 
while repeat:
    x = int( input("Enter integer x: ")) 
    y = int( input("Enter integer y: ")) 
    try:
        result = x/y
        print(f"{x} divided by {y} is {result}")
        repeat = False # Terminates loop 
    except ZeroDivisionError:
        print("Dividing by zero, try again ...\n")

#




