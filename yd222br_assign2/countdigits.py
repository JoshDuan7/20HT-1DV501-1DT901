import sys

N = input('Enter a large positive integer: ')

if int(N) < 0:
    sys.exit('Input must be positive!')

num_zero, num_odd, num_even =0, 0, 0
for num in N:
    if num == '0':
        num_zero += 1
    elif (int(num) % 2) != 0:
        num_odd += 1
    elif (int(num) % 2) == 0:
        num_even += 1
print('Zeros: ',num_zero)
print('Odd: ',num_odd)
print('Even: ',num_even)

