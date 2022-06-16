
def count_different(lst):
    st = set(lst)
    return st

def count_occurrences(lst):
    count = {}
    for i in lst:
        if i not in count:
            count[i] = 0
        count[i] += 1
    # for showing frequencies from high to low
    count = dict(sorted(count.items(),key=lambda item:item[1],reverse=True)) 
    a = 0 
    for k,v in count.items():
        a += 1
        print(f"{k}:{v}",end="  ")
        if a % 10 == 0:
            print() # for line change

try:        
    path_a = "10000_integers/file_10000integers_A.txt"
    path_b = "10000_integers/file_10000integers_B.txt"
    
    with open (path_a,"r") as file:
        num_lstA = []
        for lines in file:
            num_lstA.extend( [int(i) for i in lines.split(",")] )
        num_lstA.sort() # for better presentation of figures
        st = count_different(num_lstA)
        print( "Set_A from 'file_10000integers_A':\n",st )  
        print( "\nNumber and occurrances from 'file_10000integers_A.txt': " )
        count_occurrences(num_lstA)
        print( "\n" )
    
    with open (path_b,"r") as file:
        num_lstB = []
        for lines in file:
            num_lstB.extend( [int(i) for i in lines.split(":")] )
        num_lstB.sort() # for better presentation of figures
        st = count_different(num_lstB)
        print( "Set_B from 'file_10000integers_B':\n", st)
        print( "\nNumber and occurrances from 'file_10000integers_B.txt': " )
        count_occurrences(num_lstB)
except FileNotFoundError as e:
    print (e)