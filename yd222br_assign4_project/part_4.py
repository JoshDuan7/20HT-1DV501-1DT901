import matplotlib.pyplot as plt
import os
import word_set as ws
import table as tbl
import divide_text_into_words_new as dvi
import time

try:
    print("task 1")
    # for table.py
    # Measure the time to look-up X thousand elements (keys) in maps of different
    # sizes (larger than X) in your binary search tree based table implementation.

    eng_lst = os.getcwd()
    eng_lst +="/fe222pa_assign3/temp/large_texts.txt/eng_news_100K-sentences.txt" #eng_news txt file.

    eng_lst = dvi.read_words(eng_lst)

    w_s = ws.new_empty_set()
    r_s = tbl.new_empty_root()

    for i in eng_lst:
        ws.add(w_s, i)
    keys = []

    for i in w_s:
        for n in i:
            keys.append(n)

    n = int(input("input Thousand elements(*1000): "))
    n = n*1000
    r = 0
    l = 0
    j = 0
    max_depth = []
    table_size = []
    tb_sz = []
    for i in range(ws.count(w_s)):
        tbl.add(r_s, keys[i], i)
        f =  tbl.count(r_s)
        x = tbl.max_depth(r_s)
        if r == j*100:
            table_size.append(f)
            max_depth.append(x)   
            j += 1   
        if r == l*1000 and r != n:
            tb_sz.append(f)
            l += 1
        elif r == n:
            break
        r += 1



    start = time.time()
    look_up_time = []

    a = ws.count(w_s)
    repeat = 50
    if n > a:
        print("Error, higher key values than in the text itself.")
    else:
        while n > 0:
            for s in range(repeat):
                for i in range(n):
                    j = tbl.get(r_s, keys[i])
            if s == repeat - 1:
                elapsed = time.time() - start
                n = n - 1000
                look_up_time.append(elapsed/repeat)
                start = time.time()


    look_up_time.sort()
    max_depth.sort()
    table_size.sort()




    plt.plot(table_size, max_depth)
    plt.title("max_depth/ table_size")
    plt.xlabel("table_size")
    plt.ylabel("max_depth")
    plt.show()

    plt.plot(tb_sz, look_up_time)
    plt.title("look up time/ table_size")
    plt.xlabel("table_size")
    plt.ylabel("look up time[s]")
    plt.show()

    print("-----------------------------------------------------------------------------------------------------------------------")

    # # ----------------------------------------------------------------------------------------------------------------------------------
    print("task 2")
    # keys

    repeat = 100 # 1000 for better results just takes longer.
    time_it_takes_to_add_1000_unique_elements = []
    max_bucket_size = []
    set_sizes = []

    start = 0 
    start = time.time()
    word_set = ws.new_empty_set()
    start = time.time()
    word_set1 = word_set
    k = 0
    l = 1001
    print(a)
    while l < a:
        for n in range(repeat):
            for i in range(k, l):
                ws.add(word_set, keys[i])
            if n != repeat - 1:
                word_set = word_set1
            else:
                pass
        elapsed = time.time() - start
        m = ws.bucket_list_size(word_set)
        j = ws.max_bucket_size(word_set)
        max_bucket_size.append(j)
        set_sizes.append(m)
        word_set1 = word_set
        time_it_takes_to_add_1000_unique_elements.append(elapsed/repeat)
        start = time.time()
        k += 1000
        l += 1000


    plt.plot(set_sizes, max_bucket_size)
    plt.xlabel("set_sizes")
    plt.ylabel("max bucket size")
    plt.title("max_bucket_sizes vs set_sizes")
    plt.show()


    plt.plot(set_sizes, time_it_takes_to_add_1000_unique_elements )
    plt.xlabel("set_sizes")
    plt.ylabel("time_it_takes_to_add_1000_unique_elements[s]")
    plt.title("time_it_takes_to_add_1000_unique_elements vs set_sizes")
    plt.show()
except FileNotFoundError as f:
    print(f)
except Exception as f:
    print(f)