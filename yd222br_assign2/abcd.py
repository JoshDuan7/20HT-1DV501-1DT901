def produce_abcd():
    for A in range (1,10):
        for B in range (0,10):
            for C in range (0,10):
                for D in range(1,10):
                    if (A * 1000 + B * 100 + C * 10 + D) * 4 == D * 1000 + C * 100 + B * 10 + A:
                        print(A,B,C,D,sep=",")

def get_number(a,b,c,d):
    number = a * 1000 + b * 100 + c * 10 + d
    return number

produce_abcd()
a = int(input("please input number a: "))
b = int(input("please input number b: "))
c = int(input("please input number c: "))
d = int(input("please input number d: "))
num = get_number(a,b,c,d)
print(num)

