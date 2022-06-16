************************

# Mini-project report 
Members: Yuyao Duan, Fredric Eriksson Sepúlveda, and Melat Getachew Haile  
Program: Software Technology  
Course: 1DV501 
Date of submission: 2020-10-30

## Introduction  
The Mini-Project task is an important part of Introduction to Programming Course 1DV501/1DT901 which including comprehensive knowledge of this course. The project is conducted through Python programming language. The source code management platform GitLab has been applied for project planning throughout the task. The large text files are used for testing to provide the data source. In the first part, File IO technique along with the words split function have been implemented. Two main data structures, including a set based on hasing and a table based on binary search tree, are developed in the second part of the project. All the data structures are designed to fulfill the project's requirements and limitations. By implementation of part two, part three related to words analysis in terms of counting unique words, present a histogram and identifying top-10 most frequently used words are given. matplotlib Furthermore, the time measurements related to program efficiency for binary search tree based table and hash set implementations are given in part four.

## Part 1: Divide text into words
- Definition of a word in this project:

In part one, the program is developed for identifying every English word in a large text and saving them in a list. We define a word in our program following the normal English grammatical habits, that is, a single distinct meaningful element (consisting of the 26 English alphabets) of speech or writing, together with others (or sometimes alone) to form a sentence and typically shown with a space on either side when written or printed. Moreover, this program also identifys abbreviations, such as "I'm", "can't", "You've", "Where'd" etc. Each of them is considered as a word. Another situation we detected is that two or more words connected via hyphen which is also considered as a word e.g. "thirty-seven", "non-migratory", "CART-MASTER", "bi-weekly" etc. Even each of these consists of more than one common word, but each of these compound words in English grammer is considered as one word.

In order to have a proper understanding of dividing large text, we firstly opened the text files and went through content. This helped us to design a fitting algorithm to capture the target words based on our definition and filter the other characters. Our test objects include two files ``holy_grail.txt`` (Grail) and ``eng_news_100K-sentences.txt`` (news_100k). We used ``re`` module's ``re.split()`` function to split each line of the text.
```python
import re 
def read_words(inputfile):
    with open(inputfile, 'r',encoding='utf-8') as f:
        content = f.read()
		words = re.split('\ |\.|\/|\n',content)
```
We found that the conventional ``split()`` function 
```python
words = content.split()
```
is not sufficient to handle the complicated content such as the words embedded in a URL which normally using ``"/"`` and ``"."`` to seperate different words. For example, an URL was identified in news_100k as follows:
```
www.forbes.com/taiwan
```
The best way to get these words from large text is through implementing multi-splitting conditions to divide each line. In the ``re.split()`` function, users can use ``"|"`` to set up different conditions to split the content. From left to right includes four conditions to divide the sentences in the texts, they are ``"\ "``(space),``"\."``(period, typically for URL),``"\/"``(slash, mainly for URL), and ``"\n"``(new line, to avoid some words in the end of sentences with capture mistakes).

After using these conditions to split the lines in the text file, the massive chunks from the text need to be filtered, these abandoned contents including non-English words, numbers, ``"-"`` in the beginning or end of the words. Also this selection should keep the abbreviated words which are included a ``"'"`` in the word.
```python
for word in words:   
	for i in word:
		# 39 is "'"
		if ord( i )<39:
			word = word.replace(i,'')
		# 45 is "-" in the middle of a word
		if 39<ord( i )<45:
			word = word.replace(i,'')
		# 65 is "A"
		if 45<ord( i )<65:
			word = word.replace(i,'')
		# 90 is "Z"
		# 97 is "a"
		if 90<ord( i )<97:
			word = word.replace(i,'')
		# 122 is "z"
		if ord( i )>122:
			word = word.replace(i,'')
		# remove "-" at the end of the word
		if word.endswith('-'):
			word = word.replace('-','')
		# remove "-" at the beginning of the word
		if word.startswith('-'):
			word = word.replace('-','')
		if word == "'":
			word = word.replace("'",'')
	if word != "":
		lst.append(word)
```
We used ASCII code to spot each of the element within the language block. We know the ASCII of ``"'"`` is 39 and ``"-"`` is 45, so ASCII smaller than 39 or between 39 and 45 should be replaced with ``""`` as empty string.
We use this strategy to filter unwanted items. The same implication for English letters (both upper and lower case). After this, if a word starting or ending with a ``"-"``, we also need to remove them as above. In the end, we append the non-empty string in our list.

After implentation this algorithm， the following table shows the words we counted from the two large text files.

|   File Name                    |     Unique Word Count     |
|:-------------------------------|-------------------:|
| ``holy_grail.txt``             |         2235       |
| ``eng_news_100K-sentences.txt``|        104507      |


## Part 2: Implementing data structures
- Project requirements and limitations for implementing the data structures:

There are two data structures are required in part two: the one is a hash-based set by using a list with an initial size of 10 which will double its size when the amount of the added elements equals to the size of the list; another data structure is an application of binary search tree based on lists of size 4 which the new node will be added in the tree based comparing the keys in the lists.

- Hash based word set, implementation of the ``add`` function:

In this ``add`` function, we iterated the ``word``variable which is obtained from it and calculated the ASCII of each letter. Meanwhile, during the iteration, we also give each of the letter with a weight based on its order in the word, namely, the first alphabet in the word with a weight of 1, the second with 2, the third with 3 etc. We accumulated the value of each letter's ASCII code multiplying its weight. Then we used the accumulation ``Mod`` or modulo (``"%"``) the current size of the list to compute the position in the list. The program will compare the elements already in the list and length of current list. Once the number of elements equals to the size of the list, the current list will double its size and the previous elements will be firstly copyed to another temporary list and later on be copyed to this new doubled list.

The one main difference we got in the beginning is the value of ``"Max bucket:"``, which in our case in the begining is 3 instead of 2 from the sample. The reason for this difference is due to we did not give weight for each letter, which led more words with same position (the ASCII summation ``Mod`` the length of list). The later improvement made each of the word's total weighted ASCII more unique comparing other words. This finally achieved the result of ``"Max bucket: 2"`` instead of ``"3"``.

By implementation of this data stucture, we calculated the max bucket size of each file as follows:

|   File Name                    |     Max Bucket Size     |
|:-------------------------------|------------------------:|
| ``holy_grail.txt``             |           11            |
| ``eng_news_100K-sentences.txt``|           98            |

In the ``add`` function of BST table, the lists of size 4 is applied for this data structure, each of the position is considered as (``[0]``key, ``[1]``value,``[2]``left-child, ``[3]``right-child). The root of this BST structure in the beginning will be ``[None,None,None,None]``. When the first "key-value" pair comes in, the key will be assigned to position ``[0]`` and the value will be assigned to position ``[1]``in this root list. After the root's first two spaces are occupied, the next new "key-value" pair will be assigned to either position ``[2]`` or position ``[3]`` which is decided by the comparison of new key and the key in the root's list. If the new key equals the root's key, the new key's value will update the value of the root's key. If the new key does not equal to root's key, then after comparing the keys, if the new key smaller than the key of the root, the "key-value" pair will be added to position ``[2]`` as left-child, otherwise will be assigned to position ``[3]`` as right-child. Before adding to certain position, a new empty list may need to be added if that position is ``None``. Intuitively speaking, this BST table is like a compound list struture. In each of the layer, we used recursive algorithm to add new "key-value" pairs to the structure  which follows the logic as beginning.

Another important function in this BST table application is to count the maximum depth of the table after assigning certain data source to this structure. Again, we used recursive algorithm to retrieve the data. If the root list equals none, then the program can directly return the depth of this data structure is 0 since its root is empty.

We then used recursion to count the depth of left-child ( position ``[2]`` ) and right-child ( position ``[3]`` ) seperatedly as long as this list does not equal to empty. We use built-in founction ``"max()"`` to compare the result of left-child and the result of right-child and plus 1 ( since the depth of the root should be counted in ) to the final result.

The only one difference from the given results in ``table_main.py`` ( or can say as a potential mistake ) is that we initially used "value" instead of "key" in the "key-value" pairs to compare for positioning left-child or right-child. This caused the data structure is different from requirements of the task. It led to one more layers in this BST table when testing the ``table_main.py`` comparing to the result from the instruction.

The maximum depth we retrieved when adding words from Grail and news_100k as follows:

|   File Name                    |     Maximum Depth       |
|:-------------------------------|------------------------:|
| ``holy_grail.txt``             |            28           |
| ``eng_news_100K-sentences.txt``|            44           |

## Part 3: Word related exercises
For each subtask, there were 3 subtasks to take into consideration:

The first task: it was to obtain the amount of unique words by using the word_set.py file, and using the ``count(word_set)`` function rather simple, just create an empty word_set by using the function ``new_empty_set()`` and equating it to a variable called ``word_set`` and simply ``ws.add(word_set, (each word in the list))``and each word is obtained by using the ``divide_text_into_words_new.py``, function, ``read_words(file)``
then use ``ws.count(word_set)`` in order to answer the task.

The second task: Counting all words in each line and append it to a list:
``` python
l = 0
letters = []
o = 0
for i in read_holy_grail:
    for z in i:
        o += 1
    if l < o:
        l = o
    letters.append(o)
```

Then create bins for all the values:
Its made by adding 0.5 at an empty list calles bins and it stops when the ``"range = l"``, the largest word in terms of letters and we added 0.5 because its more convenient and then to plot:

```python
plt.xlabel("words of a given length")
plt.ylabel("frequency")


plt.hist(letters, bins=bins, edgecolor = "black", log = True)
plt.title("Histogram of eng_news_100K_-Sentences.txt")
plt.show()
```
We made a logarithmic graph because the smallest values are hidden otherwise.

The last but not least, for task 3, we organized all values by counting their occurrence in the list and then implemented those values to 2 different lists:
The first for words and the second for amount of occurences then added them to the functions in table.py in the same function, hence ```tbl.add(root_(text), g, l)```, ```g``` is word, ```l``` is ammount of ocurrences.

Then we used the fact that each pair in root was a tuple, and hence really fast at finding values therefore for the top 10 we used the largest Value - an increasing interger and everytime it could find the top 10 highest values and added it to an empty ```tuple()```, looks like this:

```python
pairs = tbl.get_all_pairs(root)
j = 0
k = tuple()
t = 0
while t < 10:
    for i in pairs:
        if longest + -1*j in i:
            k += i
            t +=1
    j +=1 
```
## Part 4: Measuring time

Task 1:
how are table size and max_depth obtained:
```python
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
```
In part 4 when adding the keys to the node, we calculated for its size and depth at specific values, size and depth: every 100 keys are added in and every 1000 keys and as long as it doesn't equal the total amount of selected keys. We then got the size, so it goes to a specific list that will be used to compare against time. All the values attached to the keys are just numbers from 0 - total keys, just to make the values easier to test at the end.

How time is calculated:
```python
if n > ws.count(w_s):
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
```
We tried to get the most reliable values of time by making it run multiple times.
and once its done with its loop, we divide it by /repeat and append it to a time_list.

We did expect the values for time to increase the higher the table_size and we thought that the depth would be increasing to a certain point, this can be the reason that the effectiveness of BST data structure.

task 2:
in order to measure the time it takes to add new elements to the hash set and also get the values for set_size and max_branch
three empty lists are made:
set_size, max_branch and time_it_takes_to_add_1000_unique_elements
then this while function is used in order to find the values to append to the lists, a is ``ws.count(word_set_of_eng_news...)``
```python
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
```
And then just use the values in a matplotlib graph:

```python
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
```
For the graph Set_sizes vs Time it takes to add 1000 unique elements:

We can infere a pattern, that being: The time consumed will become more efficient when the set of data increases, when rehashing the values of time spike but once its done with rehasing the time efficiency will become apparent.

For the graph Max bucket sizes vs set_sizes:

We can see that, the max bucket size will become more stable when the values in the set_size increase. Which means that this data structure will become more efficient the more data is added in.
## Project conclusions and lessons learned

### Technical issues 

There were a few technical challanges among different parts of our project.

In part one, we spent a lot of time to improve algorithm efficiency for news_100k. That is, developing a program to fulfill the requirements "on words" is simple but handling with large amounts of data in the real case may efficiency problem. Before we improve part one's logic, it normally costs several minutes to acquire results. It spent a lot of time to change the order for filter conditions ( the order of the if-statements ) to improve running speed.

In the second part, ``table.py``'s ``to_string()`` function did postponed our project's progession. The challenging part of this function is to have a proper understanding of principle of recurion.
```python
def get_nodes_to_string(node):
    result = ""
    if node[2] != None:
        result += get_nodes_to_string(node[2])  
    result += "(" + node[0] + "," + str(node[1]) + ")" + " "
    if node[3] != None:
        result += get_nodes_to_string(node[3])   
    return result
```
In this tree structure, the result should ``"+="`` recursive calls to retrieve whole all the data. Instead of applying this, we design the if-statements as follows:
```python
    if node[2] != None:
        get_nodes_to_string(node[2])  
    result += "(" + node[0] + "," + str(node[1]) + ")" + " "
    if node[3] != None:
        get_nodes_to_string(node[3])   
    return result
```
This small fault led this program can only retrieve two nodes of the whole BST table.

In the early stages of learning software development, discussion with teachers in the lab sessions did help us to overcome programming challenges. The solutions were normally found when having discussion with seniors in this field.

For part one, we are more interested in designing a new algorithm combining with the current one, for the samples from "news_100k" as follows:
```
PoliticsMoneyEntertainmentTechSportTravelStyleFeaturesVideo
``` 
We intended to spot the situation when traversing each letter of the long word. If the program finding an lower case is closely followed by an upper case, then we will insert a space before the upper case and split it afterwards. This can make our program more "intelligent" to target words in a large text. However, due to the time limitation, we cannot integrate this part of code with main structure very well. The ideal improvement ( code draft ) for part one as follows:
```python
for word in words:
	for j in range ( len (word)  - 1):
		if 97 <= ord(word[j]) <= 122 and 65 <= ord(word[j+1]) <= 90:
			lst_word = list(word)
			lst_word.insert(j+1," ")
			new_lst_word = ''.join(lst_word)
			word = str(new_lst_word)        
	word = re.split('\ ',word)
```
### Project issues

We organize our work by sharing workload of this project. Each of the team member was reponsible for certain parts of the project. We maintained the communication through creating Discard group and Facebook Messenger group. Both of the methods, ensured everyday's in time communication.

Yuyao Duan was responsible for part one and part two of the project and the related parts in the report. Fredric Eriksson Sepúlveda was reponsible for part three and part four of the project and related parts in the report. Melat Getachew was cooperated with Yuyao to finish part two and Fredric to finish part four.

The time consuming for this project was about 6 to 7 hours each day, we spent around 42 hours each week during the project's period.

We realized software development is responsibility-oriented work. Due to a project normally including several individual parts, each team member should be initiative with their work and be responsible for checking connection parts. In time communicating with teammates played an important role for the project task. When the cross-section problems (bugs) arised, the programmer from each part should hold a self-observation attitude for own part.


