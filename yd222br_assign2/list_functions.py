def random_list(n):
    import random
    lst = [random.randint(1,100) for i in range(n)]
    return lst

def average(lst):
    sum = 0
    for i in range (0,len(lst)):
        sum += lst[i] # sum founction
    avg = round(sum / len(lst))
    return avg

def only_odd(lst):
    odd_list=[]
    for i in range (0,len(lst)):
        if (lst[i] % 2) != 0:
            od = lst[i]
            odd_list.append(od)
    return odd_list

def to_string(lst):
    print (f'"{lst}"')

def contains(lst,a,b):
    for i in range (0,len(lst)):
        if lst[i] == a:
            if lst[i+1] == b:
                return True
    return False

def has_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    if len(new_lst) == len(lst):
        return False # it is NOT duplicated
    else:
        return True # it is duplicated



