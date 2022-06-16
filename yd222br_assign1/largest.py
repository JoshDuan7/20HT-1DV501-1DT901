print('Please provide three integers A, B, C.')
A = input('Enter A: ')
B = input('Enter B: ')
C = input('Enter C: ')
if A > B and A > C:
    print('The largest number is: ', A)
if B > A and B > C:
    print('The largest number is: ', B)
if C > A and C > B:
    print('The largest number is: ', C)    
