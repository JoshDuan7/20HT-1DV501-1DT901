import random
import math
# receive points from user
n = int ( input( "Please input N: " ))
# generate random points between (-1,1)
x = []
y = []
count = 0
for i in range (0,n):
    x += [random.uniform(-1,1)]
    y += [random.uniform(-1,1)]
    if x[i]**2 + y[i]**2 <= 1: # the central point of the circle is (0,0)
        count += 1 # when the points fall in the circle then count plus  
p = count / n
pi_approx = ( 4 * p ) / ( 1 * 1 ) # ( pi * r * r ) / 2 * 2 == count / n , therefore pi = ((count / n) * 4) / (1 * 1)
pi_actual = math.pi
diff = abs(math.pi - pi_approx)
print(pi_approx)
print(diff)

