import random

# input size of this plane, if user inputs k which means 
# the values of the x and y coordinates can vary from -k to k
size = int( input( "Enter the size: " ) )
# input how many steps are allowed for each sailor
steps = int( input( "Enter the number of steps: " ) )
# input how many sailors in this simulation
sailors = int( input( "Enter the number of sailors:" ) )

# initiating the lists for storing each sailor's step status
x = []
y = []
# for receiving the random step produced by the computer

# create a counter
count = 0
# how many sailors stand on the starting point (0,0)
for i in range ( 0, sailors ):
    x += [0]
    y += [0]
for j in range ( 0, steps ):
    # producing a random step for different sailors
    
    # **REFLECTION** I feel that my algorithm is not good enough since it allows sailors 
    # continuely walking after crossing the border
    for k in range ( 0, sailors ):
        z = random.choice( [ [0,1],[0,-1],[1,0],[-1,0] ] )
        x[k] += z[0]
        y[k] += z[1]
# identifying the unlucky guys
for l in range ( 0, sailors ):
    if abs(int(x[l])) > size or abs(int(y[l])) > size:
        count += 1
fallrate = (count/sailors) * 100
print (f"Out of {sailors} drunk sailors, {count} ({'%.2f' % fallrate}%) fell into the water.")
