import random
n = random.randint(-10,10)
if n > 0 and n%2 == 0:
    print(n,'is even and positive')
if n > 0 and n%2 != 0:
    print(n,'is odd and positive')
if n < 0 and n%2 == 0:
    print(n,'is even and negative')
if n < 0 and n%2 != 0:
    print(n,'is odd and negative')