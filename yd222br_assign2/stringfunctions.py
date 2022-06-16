def concat(s,n):
    if n != 1:
        return(s+concat(s,n-1))
    else:
        return(s)

def count(s,x):
    c = 0
    for i in s:
        if i == x:
            c += 1
    return c
    
def reverse(s):
    s = ''.join(reversed(s))
    return s
    
def first_last(s):
    l = len(s) - 1
    s = s[0] + s[l]
    return s # can directly return two values

def has_two_X(s):
    count = 0
    for i in s:
        if i == "X":
            count += 1
    if count == 2:
        return True
    else:
        return False
                
def has_duplicates(s):
    l = len(s)
    i = 0
    while i != l:
        if s[i] in s[i+1:]:
            return True
        i += 1
    return False

