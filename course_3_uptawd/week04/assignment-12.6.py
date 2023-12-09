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

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

comment_sum = 0

# Retrieve all of the <span> tags
span_tags = soup('span')
for span_tag in span_tags:
    # one way to get the attributes of the span tag
    #if span_tag.get('class', None) != None:
        #print('Span:', span_tag.get('class', None)[0])

    # another way to get the attributes of the span tag
    #if 'class' in span_tag.attrs:
        #print('Attrs:', span_tag.attrs['class'][0])

    print("Count ", span_tag.contents[0])
    comment_sum = comment_sum + int(span_tag.contents[0])

print("Sum ", comment_sum)