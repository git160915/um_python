fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try :
    fh = open(fname)
except :
    print("Error: File not found with path/filename:", fname)
    quit()

email_list = list()

for line in fh :
    if line.startswith("From ") :
        word_list = line.strip().split()
        email_list.append(word_list[1])
        print(word_list[1])

count = len(email_list)

print("There were", count, "lines in the file with From as the first word")
