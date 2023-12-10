import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: quit()

params = dict()
params['address'] = address
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

count_of_count_elements = 0
sum_of_count_element_values = 0

results = tree.findall('.//count')
for result in results:
    count_of_count_elements = count_of_count_elements + 1
    try:
        sum_of_count_element_values = sum_of_count_element_values + int(result.text)
    except:
        print("Error: Value found in element <count> was not an integer.")
        quit()

print("Count:", count_of_count_elements)
print("Sum:", sum_of_count_element_values)