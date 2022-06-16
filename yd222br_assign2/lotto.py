import random

lst = []
for i in range (0,7):
    rn = random.randint(1,35)
    if i == 0:
        lst.append(rn)
    else:
        while rn == lst[i-1]:
            rn = random.randint(1,35)  
        lst.append(rn)
print(lst)

