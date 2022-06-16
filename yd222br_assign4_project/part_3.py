import word_set as ws
import table as tbl
import divide_text_into_words_new as dvi
import os
import matplotlib.pyplot as plt



    # This part to identify that how many unique words that are used in the texts.
    # holy_grail
try:
    print("\ntask 1")
    holy_grail = os.getcwd()
    holy_grail += "/fe222pa_assign3/temp/large_texts.txt/holy_grail.txt"
    english_texts = os.getcwd()
    english_texts += "/fe222pa_assign3/temp/large_texts.txt/eng_news_100K-sentences.txt" 


    read_holy_grail = dvi.read_words(holy_grail)
    lst_holy_grail = ws.new_empty_set()
    for i in read_holy_grail:
        ws.add(lst_holy_grail,i)

    delete = ["'"]
    for i in delete:   
        ws.remove(lst_holy_grail,i)

    holy_word_count = ws.count(lst_holy_grail)
    print("--------------------------------------------------------------")
    print("Unique words in 'holy_grail.txt': ",holy_word_count)


    # eng_news_100K-sentences
    read_news = dvi.read_words(english_texts)
    lst_news = ws.new_empty_set()
    for i in read_news:
        ws.add(lst_news,i)


    for i in delete:   
        ws.remove(lst_news,i)

    news_word_count = ws.count(lst_news)
    print("Unique words in 'eng_news_100K-sentences.txt': ",news_word_count)
    print("--------------------------------------------------------------")



    l = 0
    letters = []
    o = 0
    for i in read_holy_grail:
        for z in i:
            o += 1
        if l < o:
            l = o
        letters.append(o)
        o = 0
    bins = []

    for i in range(1, l + 2):
        i += -0.5
        bins.append(i)



    plt.xlabel("words of a given length")
    plt.ylabel("frequency")


    plt.hist(letters, bins=bins, edgecolor="black", log=True)
    plt.title("Histogram of Holy_grail.txt")
    plt.show()


    l = 0
    letters = []
    o = 0
    for i in read_news:
        for z in i:
            o += 1
        if l < o:
            l = o
        letters.append(o)
        o = 0
    bins = []

    for i in range(1, l + 2):
        i += -0.5
        bins.append(i)




    plt.xlabel("words of a given length")
    plt.ylabel("frequency")


    plt.hist(letters, bins=bins, edgecolor="black", log=True)
    plt.title("Histogram of eng_news_100K_-Sentences.txt")
    plt.show()



    # ----------------------------------------------------------------------------------------------


    print("task 3")
    root_Holy_grail = tbl.new_empty_root()




    words = []
    nmb = []
    l = 0
    longest = 0
    g = ""
    k = ""
    for i in lst_holy_grail:
        for n in i:
            for d in read_holy_grail:
                if n == "":
                    pass
                else: 
                    if n == d:
                        g = d
                        l += 1 
                    if longest < l:
                        longest = l
            tbl.add(root_Holy_grail, g, l)
            l = 0 


    pairs = tbl.get_all_pairs(root_Holy_grail)              
    j = 0
    k = tuple()
    t = 0
    while t < 10:
        for i in pairs:
            if longest + -1*j in i:
                k += i
                t +=1
        j +=1 
    print("-------------------------------------------------------------------------------------")
    print("The top 10 words in holy_grail.txt are: ", k)



    root_eng_text = tbl.new_empty_root()




    words = []
    nmb = []
    l = 0
    longest = 0
    g = ""
    k = ""
    for i in lst_news:
        for n in i:
            for d in read_news:
                if n == "":
                    pass
                else: 
                    if n == d:
                        g = d
                        l += 1 
                    if longest < l:
                        longest = l
            tbl.add(root_eng_text, g, l)
            l = 0 

    pairs = tbl.get_all_pairs(root_eng_text)             
    j = 0
    k = tuple()
    t = 0
    while t < 10:
        for i in pairs:
            if longest + -1*j in i:
                k += i
                t +=1
        j +=1 

    print("The top 10 words in eng_news_100K-sentences.txt are: ", k) #takes around 40 minutes, tried everything, its the fastest it goes.

    print("Max depth:", tbl.max_depth(root_eng_text))  

    print("-------------------------------------------------------------------------------------")
except FileNotFoundError as f:
    print(f)
except Exception as f:
    print(f)