import os 

# function for counting lines of each .py file
def count_py_lines(file_name):
    with open (file_name, "r") as file:
            #print(file_name)
            line_count = 0
            for line in file:
                if not line.split(): # identify if it is empty lines
                    line.strip() # remove "\n"
                    continue
                else:
                    line_count += 1
    return line_count

# function for identifying all .py files
def find_files(dir_path, allfile):
    entries = os.scandir(dir_path)
    for filename in entries:
        if filename.is_dir():
            find_files (filename, allfile)
        if filename.name.endswith(".py"):
            allfile.append (filename)
    return (allfile)

try:
    # program starts here
    path = os.getcwd() # to count all .py file from the folder 'assign3'
    lst = find_files(path, []) # save all the .py files in this list 
    count = 0
    # using this loop to count how many lines of codes in total
    for s in lst: 
        count += count_py_lines(s) 
    # present the final result
    print("path =", path)
    print("Python Line Count:", count)
except FileNotFoundError as e:
    print(e)
