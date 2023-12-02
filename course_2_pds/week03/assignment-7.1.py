# Use words.txt as the file name
fname = input("Enter file name: ")

try :
    fh = open(fname)
except :
    print("Error: File does not exist with path/filename:", fname)
    quit()

file_contents = fh.read()
print(file_contents.upper().strip())