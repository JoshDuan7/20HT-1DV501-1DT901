def is_palindrome(s):
    new_s = ""
    for i in s:       
        new_s += i.lower()
    new_s = "".join(j for j in new_s if j.isalnum())
    p = 0
    q = len(new_s)-1
    if q <= p:
        return True
    while p <= q:
        if new_s[p] != new_s[q]:
            return False
        p += 1
        q -= 1
    return True
    
x = is_palindrome("Was it a rat I saw?")
print(x)

x = is_palindrome("What is that?")
print(x)