# A list based hash table implementation for strings.
# Initial bucket size is 10, we double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set(): # This part is from teacher
    global size
    size = 0
    buckets = []
    for _ in range(10):
        buckets.append([])
    return buckets

# Adds word to word set if not already added
def add(word_set, word):
    global size # count for how many elements in the buckets
    temp = [] # when the bucket rehashing, we need this list temporarely keeping the first 10 elements
    hash_value = 0
    x = 0
    for i in word:  # calculate word's hash value
        x += 1   # weight for each ASCII
        hash_value += ( ord(i) * x )
    b_size = bucket_list_size(word_set) # get the length of current bucket
    position = hash_value % b_size
    if word not in word_set[position]: # to filter duplicate words
        word_set[position].append(word) # add new words
        size += 1 # count elements have added in the list
        if size == b_size: # when the added elements equals to the current bucket's size then double the bucket 
            for j in word_set:
                for k in j:
                    temp.append(k) # copy the first 10 to temp[]
            word_set.clear() # clear previous word_set
            for _ in range(b_size*2): # double the size
                word_set.append([])
            b_size = bucket_list_size(word_set)
            for te in temp: # copy temp to new expand list
                rehash_value = 0
                x = 0
                for te_ in te:
                    x += 1
                    rehash_value += ( ord(te_) * x )
                position = rehash_value % b_size
                word_set[position].append(te)
    return word_set
    


# Returns current number of elements in set
def count(word_set):
    return size

# Returns current size of bucket list
def bucket_list_size(word_set):
    bucket_size = len(word_set)
    return bucket_size

# Returns a string representation of the set content
def to_string(word_set):
    result = "{ "
    for i in word_set:
        for j in i:
            if not []: # e.g. to identify list like this [["abc"]["efg"]["huy"][]] , filter the inside empty list
                result += str(j) + " "
    return result + "}"

# Returns True if word in set, otherwise False    
def contains(word_set, word): 
    hash_value = 0
    x = 0
    for i in word: # calculate the word's hash_value then finding the position, in the position to find it
        x += 1 # weight for each ASCII
        hash_value += ( ord(i) * x )
    position = hash_value % bucket_list_size(word_set)
    if len(word_set[position]) != 0:
        for j in word_set[position]:
            if word == j:
                return True 
            else:
                return False

# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word): # same as function 'contains'
    global size
    flag = contains(word_set, word)
    if flag == True:
        hash_value = 0
        x = 0
        for i in word:
            x += 1 # weight for each ASCII
            hash_value += ( ord(i) * x )
        b_size = bucket_list_size(word_set)
        position = hash_value % b_size
        for j in word_set[position]:
            if j == word:
                word_set[position].remove(j)
                size -= 1              
    return word_set


# Returns the size of the bucket with most elements
def max_bucket_size(word_set): # search each of the list in the word_set
    max = 0
    for i in word_set:
        if len(i) > max:
            max = len(i)
    return max
