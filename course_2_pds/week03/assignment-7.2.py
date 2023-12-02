# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try :
    fh = open(fname)
except :
    print("Error: File does not exist with path/filename:", fname)
    quit()

count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    count = count + 1
    num_str = line[line.find(":") + 1:].strip()

    try :
        num_float = float(num_str)
    except :
        print("Error: String does not store a floating number:", num_str)
        quit()

    total = total + num_float
print("Average spam confidence:", total / count)
