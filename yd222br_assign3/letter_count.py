
def count_letter_occurrences(lst):
    dct = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,\
        "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for i in lst:
        i = str(i).lower()
        if i == 'a':
            dct["a"] += 1
        elif i == 'b':
            dct["b"] += 1
        elif i == 'c':
            dct["c"] += 1
        elif i == 'd':
            dct["d"] += 1
        elif i == 'e':
            dct["e"] += 1
        elif i == 'f':
            dct["f"] += 1
        elif i == 'g':
            dct["g"] += 1
        elif i == 'h':
            dct["h"] += 1
        elif i == 'i':
            dct["i"] += 1
        elif i == 'j':
            dct["j"] += 1
        elif i == 'k':
            dct["k"] += 1
        elif i == 'l':
            dct["l"] += 1
        elif i == 'm':
            dct["m"] += 1
        elif i == 'n':
            dct["n"] += 1
        elif i == 'o':
            dct["o"] += 1
        elif i == 'p':
            dct["p"] += 1
        elif i == 'q':
            dct["q"] += 1
        elif i == 'r':
            dct["r"] += 1
        elif i == 's':
            dct["s"] += 1
        elif i == 't':
            dct["t"] += 1
        elif i == 'u':
            dct["u"] += 1
        elif i == 'v':
            dct["v"] += 1
        elif i == 'w':
            dct["w"] += 1
        elif i == 'x':
            dct["x"] += 1
        elif i == 'y':
            dct["y"] += 1
        elif i == 'z':
            dct["z"] += 1
    return dct

path_a = "large_texts/holy_grail.txt"
path_b = "large_texts/eng_news_100K-sentences.txt"

try:
    with open (path_a,"r") as file:
        letter_lst_a = []
        for lines in file:
            letter_lst_a += lines
        dct_a = count_letter_occurrences(letter_lst_a)
        print( "\nReading text from the file: ", path_a)
        print( "Total number of letters: ",sum( dct_a.values() ) )
        print( "\nHistogram (where each star represents 50 occurrences)" )
        for k,v in dct_a.items():
            print(k," | ", "*"*(v//50))
    print("\nSecond file is processing (12 sec) ...  ")

    with open (path_b,"r") as file: # running this part may take longer time, please be patient!
        letter_lst_b = []
        for lines in file:
            letter_lst_b += lines
        dct_b = count_letter_occurrences(letter_lst_b)
        print( "\nReading text from the file: ", path_b)
        print( "Total number of letters: ",sum( dct_b.values() ) )
        print( "\nHistogram (where each star represents 10000 occurrences)" )
        for k,v in dct_b.items():
            print(k," | ", "*"*(v//10000))
        print(">>>Conclusion: from the pattern we can see the two files has the same character frequency! ")
except FileNotFoundError as e:
    print (e)