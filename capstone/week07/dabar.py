import sqlite3
import time
import zlib

dbname = input("Please provide the sqlite DB filename to load: ")
if (len(dbname) < 1) : dbname = "raw_content.sqlite"
top_x = input("How many top EV makers would you like to visualize (e.g. for top 10, enter: 10).  For everything, enter (-1): ")
try:
    top_x = int(top_x)
except:
    print("WARNING: Must enter an Integer for top EV makers.  Proceeding with default of top 10")
    top_x = 10

connection = sqlite3.connect(dbname)
cursor = connection.cursor()

cursor.execute('''
    SELECT COUNT(*)
    FROM raw_ev_population_data
    ''')
total_ev_population = float(cursor.fetchone()[0])

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
count = 0
count_other = 0
other_category_size = 0

fhandler = open("dabar.js", "w")
fhandler.write("dabar = [['Make', 'Number of Registered EVs', {role: 'annotation'}]")
for k in x[:100] :
    size = counts[k]
    percentage_of_population = (size / total_ev_population) * 100
    #size = (size - lowest) / float (highest - lowest)
    #size = int((size * bigfontsize) + smallfontsize)
    if (count < top_x or top_x == -1) :
        fhandler.write(",\n")
        fhandler.write("['" + k + "', " + str(size) + ", '" + str(size) + f" ({percentage_of_population:.2f}%)'" + "]")
    else :
        count_other += 1
        other_category_size += size
    count += 1

if (top_x > 0) :
    fhandler.write(",\n")
    percentage_of_population = (other_category_size/ total_ev_population) * 100
    fhandler.write("['Other " + str(count_other) + " EV makers', " + str(other_category_size) + ", '" + str(other_category_size) + f" ({percentage_of_population:.2f}%)'" + "]")

fhandler.write("\n];\n")
fhandler.close()

print("Output writtein to dabar.js")
print("Open dabar.htm in a browser to see the visualisation")