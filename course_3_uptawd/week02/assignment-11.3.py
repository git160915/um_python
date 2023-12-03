import re

# fname = "regex_sum_42.txt"
fname = "regex_sum_1939383.txt"

try :
    handle = open(fname)
except :
    print("Error: File not found with path/filename:", fname)
    quit()

file_contents = handle.read()
num_list = re.findall('([0-9]+)', file_contents)
sum = 0

for num in num_list :
    sum = sum + int(num)

print(sum)