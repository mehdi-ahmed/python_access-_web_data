# download ds4 from https://www.py4e.com/code3/
# and unzip at same folder as this file

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
