import re 
def read_words(inputfile):
    with open(inputfile, 'r',encoding='utf-8') as f:
        content = f.read()
        words = re.split('\ |\.|\/|\n',content)
        lst = []
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
        return lst


