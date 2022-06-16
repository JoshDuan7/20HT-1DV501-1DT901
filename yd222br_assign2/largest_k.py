import sys

s = 0
k = 0

n = int(input('Enter a positive integer: '))
if n < 0:
    sys.exit('Input must be positive!')
while s <= n-k:
    s = s + k
    k += 2
    #print(s,k)
print(k-2,'is the largest k such 0+2+4+6+...+k <',n)

