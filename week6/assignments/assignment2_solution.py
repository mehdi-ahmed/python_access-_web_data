# https://www.py4e.com/tools/python-data/?PHPSESSID=f535f0377918c8b21c65c1dbd3ff49eb

# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that
# data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a
# place as within Google Maps.


import json
import urllib.parse
import urllib.request
from json import JSONDecodeError

service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

address = input('Enter Location: ')  # rue de l'Artichaut
if len(address) < 1:
    address = 'University of Helsinki'

url = service_url + urllib.parse.urlencode({'address': address})
print(url)

params = dict()
params['address'] = address
params['key'] = api_key
url = service_url + urllib.parse.urlencode(params)
print('Retrieving url:', url)  # http://py4e-data.dr-chuck.net/json?address=University+of+Helsinki&key=42

uh = urllib.request.urlopen(url)
data = uh.read().decode()

print('Retrieved: ', len(data), 'characters')

try:
    js = json.loads(data)
except JSONDecodeError:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('-----! Failure to retrieve !------')
    print(data)

for item in js['results']:
    print('Place id', item["place_id"])
