import sqlite3
import time
import zlib

dbname = input("Please provide the sqlite DB filename to load: ")
if (len(dbname) < 1) : dbname = "raw_content.sqlite"

connection = sqlite3.connect(dbname)
cursor = connection.cursor()

cursor.execute('''
    SELECT make, COUNT(*)
    FROM raw_ev_population_data
    GROUP BY make
    ORDER BY COUNT(*) DESC
    ''')
counts = dict()
for message_row in cursor :
    counts[message_row[0]] = int(message_row[1])

x = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for k in x[:100] :
    if highest is None or highest < counts[k] :
        highest = counts[k]

    if lowest is None or lowest > counts[k] :
        lowest = counts[k]

print('Range of counts:', highest, lowest)

# Spread the font size across 20-100 based on the count
bigfontsize = 80
smallfontsize = 20

fhandler = open("daword.js", "w")
fhandler.write("daword = [")
first = True
for k in x[:100] :
    if not first :
        fhandler.write(",\n")
    else :
        first = False
    size = counts[k]
    size = (size - lowest) / float (highest - lowest)
    size = int((size * bigfontsize) + smallfontsize)
    fhandler.write("{text: '" + k + "', size: " + str(size) + "}")
fhandler.write("\n];\n")
fhandler.close()

print("Output writtein to daword.js")
print("Open daword.htm in a browser to see the visualisation")