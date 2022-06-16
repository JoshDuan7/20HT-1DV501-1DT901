def read_words(inputfile):
    with open(inputfile, 'r') as f:
        while True:
            buf = f.read(10240)
            if not buf:
                break

            # make sure we end on a space (word boundary)
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch

            words = buf.split()
            for word in words:
                yield word
        yield '' #handle the scene that the file is empty

a = read_words("large_texts/eng_news_100K-sentences.txt")
for word in a:
    print(word)
# if __name__ == "__main__":
#     for word in read_words('./very_large_file.txt'):
#         process(word)
