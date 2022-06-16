def mult(a,b):
    if b == 1:
        return a 
    else:
        return a + mult(a,b-1)

# Program starts 
print( mult(3,7) ) 
print( mult(15,15) )