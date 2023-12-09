# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = input("Enter count: ")
position  = input("Enter position: ")
print("Retrieving: " + url)

try:
    count = int(count)
except:
    print("The parameter \"count\" must be a positive integer")
    quit()

try:
    position = int(position)
except:
    print("The parameter \"position\" must be a positive integer")
    quit()

link_depth_count = 0

while link_depth_count < count:
    link_depth_count = link_depth_count + 1

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    pos_counter = 0

    # Retrieve all of the <a> tags
    anchor_tags = soup('a')
    for anchor_tag in anchor_tags:
        pos_counter = pos_counter + 1

        if pos_counter == position:
            if 'href' in anchor_tag.attrs:
                url =anchor_tag.attrs['href']
                print("Retrieving: ", url)