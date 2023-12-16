import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving location", url)

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

try:
    info = json.loads(data)
except:
    print("Error: Failed to connect to URL,", url, ", to retrieve data.  Please double check URL.")
    quit()

print('Retrieved', len(data), "characters")

count_comments = 0
sum_comments = 0

for item in info["comments"]:
    count_comments = count_comments + 1

    try:
        sum_comments = sum_comments + int(item["count"])
    except:
        print("Error: Failed to convert integer in element \"count\".  Please double that all values are integers")
        quit()

print("Count:", count_comments)
print("Sum:", sum_comments)