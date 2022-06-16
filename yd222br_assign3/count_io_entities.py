
import os

# function for counting the directories under the path
def count_directories(dir_path):
    entries = os.scandir(dir_path)
    count_directories = 0
    for entry in entries:
        if entry.is_dir():
            count_directories += 1
    return count_directories  

# function for counting how many Python programs under the path
def count_py_files(dir_path):
    lst = os.listdir(dir_path)
    count_files = 0
    for s in lst:
        if s.endswith(".py"):
            count_files += 1
    return count_files

try:
    path = os.getcwd() # show the path from 'assign3' folder   
    print (f"\npath = {path}") # path pointing to directory containing other directories
    print ( "Dir Count:", count_directories(path) )      
    print (f"\npath = {path}") # path pointing to directory containing .py files
    print ( "Py-file Count:", count_py_files(path) )
except FileNotFoundError as e:
    print(e)