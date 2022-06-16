# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child


# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]

# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root,key,value): # 0 = key, 1 = value, 2 = left-child, 3 = right-child
    if root[0] == None: #if like this [None,None,None,None], then add the value to 0 and 1
        root[0] = key
        root[1] = value
    elif root[0] != None: # if 0 is not None, then check key if is same
        if root[0] == key: # update the key's value if key is same
            root[1] = value
        elif root[0] != key: # if not same, then choose to add to 2 or 3
            if key < root[0]: # key is smaller than 0 , left-child
                if root[2] == None: # if None then use it
                    root[2] = new_empty_root() # by creating a new empty list
                    add(root[2],key,value)
                elif root[2] != None: # if not None then 
                    add(root[2],key,value) # using recursion to create a new one
            elif key > root[0]:
                if root[3] == None:
                    root[3] = new_empty_root()
                    add(root[3],key,value)
                elif root[3] != None:
                    add(root[3],key,value)

# Returns a string representation of the table content.
# That is, all key-value pairs
def get_nodes_to_string(node):
    result = ""
    if node[2] != None:
        result += get_nodes_to_string(node[2])  
    result += "(" + node[0] + "," + str(node[1]) + ")" + " "
    if node[3] != None:
        result += get_nodes_to_string(node[3])   
    return result

def to_string(node):
    result = get_nodes_to_string(node)
    return "{ " + result + "}"
   
# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    if key == node[0]:
        return node[1]
    else:
        if key < node[0]:
            if node[2] != None:
                return get(node[2],key)
        elif key > node[0]:
            if node[3] != None:
                return get(node[3],key)
    return None

# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):
    if node == None:
        return 0
    dl = max_depth(node[2])
    dr = max_depth(node[3])
    return max(dl,dr) + 1 # +1 for root

# Returns the number of key-value pairs currently stored in the table
def count(node):
    count = 0
    result = get_nodes_to_string(node)
    for i in result:
        if i == ",": # since (key , value) always has a comma inside, then count "," for pairs
            count += 1
    return count

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
def get_root_for_pairs(root):
    tpl = ()
    if root[2] != None:
        tpl += (get_root_for_pairs(root[2])) 
    tpl += ((root[0],root[1]),) # using recursion to find all roots as tuples
    if root[3] != None:
        tpl += (get_root_for_pairs(root[3]))
    return tpl
def get_all_pairs(root):
    lst = []
    a = get_root_for_pairs(root)
    for i in a: # get each of the tuple to list
        lst.append(i)
    return lst
