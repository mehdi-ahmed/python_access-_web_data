# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.

# You are to look through all the <comment> tags and find the <count> values sum the numbers To make the code a
# little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named
# 'count' with the following line of code: counts = tree.findall('.//count')

# https://www.py4e.com/tools/python-data/?PHPSESSID=150a8febd7355b3b86ce36c81e514d13

# data = http://py4e-data.dr-chuck.net/comments_1314380.xml

import ssl
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ') # data = http://py4e-data.dr-chuck.net/comments_1314380.xml
print('Retrieving', address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')

total = 0
count = 1
for count in counts:
    total = total + int(count.text)

print('Count:', len(counts))
print('Sum:', total)
