from math import sqrt
import os

def mean(lst):
    sum = 0
    for i in lst:
        sum += int(i)
    return round( float(sum / len(lst) ), 4 )

def std(lst):
    avg_lst = mean(lst)
    sum = 0
    for i in lst:
        sum += ( ( int(i) - avg_lst ) ** 2 )
    std = sqrt ( sum / len(lst) )
    return round (std, 4)


# program start
try:
    path_A = "10000_integers/file_10000integers_A.txt"
    path_B = "10000_integers/file_10000integers_B.txt"
    
    with open (path_A,"r") as file:
        num_lstA = []
        for lines in file:
            num_lstA.extend( [int(i) for i in lines.split(",")] )
        mean_lstA = mean ( num_lstA )
        std_lstA = std ( num_lstA )
    
    with open (path_B,"r") as file:
        num_lstB = []
        for lines in file:
            num_lstB.extend( [int(i) for i in lines.split(":")] )
        mean_lstB = mean ( num_lstB )
        std_lstB = std( num_lstB )

    print("\nReading from: ",path_A)
    print("Mean:", mean_lstA)
    print("Standard deviation:", std_lstA)
    print("==========================================================")
    print("Reading from: ", path_B)
    print("Mean:", mean_lstB)
    print("Standard deviation:", std_lstB)
except FileNotFoundError as e:
    print(e)

