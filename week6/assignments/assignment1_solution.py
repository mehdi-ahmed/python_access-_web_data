# https://www.py4e.com/tools/python-data/?PHPSESSID=f6fc25ff4f704221d7a45bd6ed8cca85

# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

# Actual data: http://py4e-data.dr-chuck.net/comments_1314381.json (Sum ends with 64)

import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')  # rue de l'Artichaut
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_1314381.json'

print('Retrieving', address)

connection = urllib.request.urlopen(address, context=ctx)
data = connection.read().decode()
print('Retrieved', len(data), 'characters')

# json
js = json.loads(data)
# print(json.dumps(js, indent=4))

total = 0
count = 0
for comment in js['comments']:
    count = count + 1
    total = total + int(comment['count'])

print('Count:', count)
print('Sum:', total)
