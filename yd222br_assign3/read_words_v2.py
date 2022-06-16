def read_words(inputfile):
    with open(inputfile, 'r') as f:
        content = f.read()
        words = content.split()
        lst = []
        for word in words:
            # using ASCII to identify punctuation
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
            lst.append(word)
            for i in lst:
                if i == "":
                    lst.remove(i)
        return lst

# def read_words(inputfile):
#     with open(inputfile, 'r') as f:
#         content = f.read()
#         words = content.split()
#         lst = []
#         for word in words:
#             # using ASCII to identify punctuation
#             for i in word:
#                 # 39 is "'"
#                 if ord( i )<39:
#                     word = word.replace(i,'')
#                     lst.append(word)
#                 # 45 is "-" in the middle of a word
#                 if 39<ord( i )<45:
#                     word = word.replace(i,'')
#                     lst.append(word)
#                 # 65 is "A"
#                 if 45<ord( i )<65:
#                     word = word.replace(i,'')
#                     lst.append(word)
#                 # 90 is "Z"
#                 # 97 is "a"
#                 if 90<ord( i )<97:
#                     word = word.replace(i,'')
#                     lst.append(word)
#                 # 122 is "z"
#                 if ord( i )>122:
#                     word = word.replace(i,'')
#                     lst.append(word)
#                 # remove "-" at the end of the word
#                 if word.endswith('-'):
#                     word = word.replace('-','')
#                     lst.append(word)
#         return lst                    

lst = read_words("large_texts/holy_grail.txt")
print(lst)




