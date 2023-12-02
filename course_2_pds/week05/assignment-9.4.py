fname = input("Enter file: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try :
    handle = open(fname)
except:
    print("Error: File does not exist with path/filename:", fname)
    quit()


word_hist = dict()

for line in handle :
    if not line.strip().startswith("From ") :
        continue

    words = line.strip().split()
    word_hist[words[1]] = word_hist.get(words[1],0) + 1

most_freq_word = None
most_freq_word_count = 0

for word, count in word_hist.items() :
    if most_freq_word is None or count > most_freq_word_count :
        most_freq_word = word
        most_freq_word_count = count

print(most_freq_word, most_freq_word_count)