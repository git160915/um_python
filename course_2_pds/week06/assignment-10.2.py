fname = input("Enter file: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try :
    handle = open(fname)
except :
    print("Error: File does not exist with path/filename:", fname)
    quit()

time_dict = dict()

for line in handle :
    if not line.strip().startswith("From ") :
        continue

    time = line.strip().split()[5].split(":")
    time_dict[time[0]] = time_dict.get(time[0],0) + 1

for time, count in sorted(time_dict.items()) :
    print(time, count)