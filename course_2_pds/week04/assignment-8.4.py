fname = input("Enter file name: ")

try :
    fh = open(fname)
except :
    print("Error: File does not exist with path/filename:", fname)
    quit()

lst = list()

for line in fh :
    line_list = line.strip().split()

    for word in line_list :
        if word not in lst :
            lst.append(word)

lst.sort()
print(lst)