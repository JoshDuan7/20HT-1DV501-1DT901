import os
def read_file(file_path):
    print( "\nReading from: ", file_path )
    with open ( file_path, "r" ) as file: # safe way to open a file
        #file = open(file_path,"r") # normal way to open a file
        line_count = 0
        full_text = ""
        for lines in file:
            line_count += 1
            full_text += lines
            print( lines.strip() ) # add this to instantly show result
    print( ">>>Line count: ",line_count ) # this for showing if everything correctly has been read
    return full_text

def write_file(lines, file_path):
    with open ( file_path, "w" ) as file:
        file.write ( lines )

try:
    print( os.getcwd() )
    lines = read_file ( "Temp/do not pass me by.txt" )
    write_file ( lines, "Temp/new.txt" )
    print(">>>The file's content has been successfully written to the new file under the path 'Temp/new.txt'")
except FileNotFoundError as e:
    print (e)