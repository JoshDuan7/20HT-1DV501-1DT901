import sys

# recieve the number from user
rows = int(input("Enter an odd positive integer: "))
print()
print("Right-Angled Triangle:")
# identify if the number is fullfilled the reqirement
if rows < 0 or rows % 2 == 0:
    sys.exit("Input number is not an odd positive integer!")
# Draw the picture
for i in range(1, rows+1):
    for j in range(1, i):
        print (" ",end="")
    for k in range (0,rows+1-i):
            print ("*",end="")
    print ()
print()
print("Isosceles Triangle:")
for i in range(1,rows-2):
    for j in range(1,rows-2-i):
        print (" ",end="")
    for k in range(1,i*2):
        print ("*",end="")
    print()

    