# Assignment : https://www.py4e.com/tools/python-data/?PHPSESSID=38384132b65fabe0ebd08c4f5ce37a1f

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Actual data : http://py4e-data.dr-chuck.net/comments_1314378.html

# You need to adjust this code to look for span tags and pull out the text content of the span tag,
# convert them to integers and add them up to complete the assignment.

# Example
# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
# <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
# <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

import ssl
from urllib.request import urlopen

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum_span_numbers = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    sum_span_numbers = sum_span_numbers + int(tag.contents[0])
    count = count + 1

print('Count', count)
print('Sum', sum_span_numbers)
