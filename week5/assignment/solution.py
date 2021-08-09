# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
# comment counts from the XML data, compute the sum of the numbers in the file.

# You are to look through all the <comment> tags and find the <count> values sum the numbers To make the code a
# little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named
# 'count' with the following line of code: counts = tree.findall('.//count')

# https://www.py4e.com/tools/python-data/?PHPSESSID=150a8febd7355b3b86ce36c81e514d13

import ssl
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/xml?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    if api_key is not False:
        params['key'] = api_key

    url = service_url + urllib.parse.urlencode(params)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)
    #
    # results = tree.findall('result')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
    #
    # print('lat', lat, 'lng', lng)
    # print(location)
