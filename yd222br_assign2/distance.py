from math import sqrt

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
print("The distance between"+"(",x1,",",y1,") and (",x2,",",y2,") is",round(distance,3))