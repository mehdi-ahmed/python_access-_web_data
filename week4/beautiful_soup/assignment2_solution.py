# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import ssl
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')

print('Retrieving:', url)  # http://py4e-data.dr-chuck.net/known_by_Madinah.html

count_loop = 1
while True:
    tag_position = tags[position - 1]
    new_url = tag_position.get('href', None)

    print('Retrieving:', new_url)
    if count_loop == count:
        break

    count_loop = count_loop + 1
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')

# TODO: improve this and get rid of repetitive code
