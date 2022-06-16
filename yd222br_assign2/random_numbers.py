import random

sum = 0
r1 = 0 # to save max
r2 = 0 # to save min
num = int( input( "Enter number of integers to be generated:"  ) )

print("Generated values: ",end="")
for i in range (num):
    r = random.randint(1,100)
    print(r,end=" ")
    if r > r1:
        r1 = r
    if i == 1: # first time assign min value for later compare 
        r2 = r
    if r < r2:
        r2 = r 
    sum += r
avg = sum / num
max = r1
min = r2
print()
print("Average, min, and max are ",avg,",",min,","+"and",max)
