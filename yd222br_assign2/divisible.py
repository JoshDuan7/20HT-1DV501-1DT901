k = 0
for i in range(100,200,1): 
    if (i%4==0 and i%5!=0) or (i%5==0 and i%4!=0):
        print(i, end=' ')
        k = k + 1
        if k % 10 == 0:
            print('')
            

        
         
            

       

