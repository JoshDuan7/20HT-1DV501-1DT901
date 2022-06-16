import sys

s = 0
k = 1

n = int(input('Enter a positive integer: '))
if n < 1:
    sys.exit('Input must be positive and over than 1!')
while s+k < n:
    s = s + k
    k += 2
    #print(s,k)
print(k,'is the smallest k such 1+3+5+7+...+k >=',n)


