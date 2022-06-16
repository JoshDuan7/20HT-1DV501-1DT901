identifier = str(input('Enter a chess square identifier (e.g. e5): '))
id1=str(identifier[0])
id2=str(identifier[1])
if id1=='a' or id1=='c' or id1=='e' or id1=='g':
    if int(id2)%2==0:
        print(identifier,'is White')
    else:
        print(identifier,'is Black')
if id1=='b' or id1=='d' or id1=='f' or id1=='h':
    if int(id2)%2==0:
        print(identifier,'is Black')
    else:
        print(identifier,'is White')
    
