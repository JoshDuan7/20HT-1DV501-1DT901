sz = int ( input("Enter an integer 3 or higher: "))

if sz < 3: # Check input 
    print("The size must 3 or higher") 

else:
# Two types of square lines 
    stars = "" 
    for i in range(sz):
        stars += "*"

    line = "*"
    for i in range(sz-2):
        line += " " 
    line += "*"

    #Print square 
    print("\nThe square for number", sz) 
    print(stars) 
    for i in range(sz-2):
        print(line) 
    print(stars)