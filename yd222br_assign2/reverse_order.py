print("Enter positive integers. End by giving a negative integer.")
positive_integer = []
n = 0
while True:
    n += 1
    x = int(input(f"Integer {n}: "))
    if x > 0:
        positive_integer.append(x)
    else:
        break
positive_integer.reverse()
print(positive_integer)
