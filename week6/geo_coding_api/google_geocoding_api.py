# Geocoding API
# https://developers.google.com/maps/documentation/geocoding/overview

# Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into
# geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers on a
# map, or position the map.

# Example: Rue de l'Artichaut
# https://maps.googleapis.com/maps/api/geocode/json?&address=Rue%20de%20l%27Artichaut

# Remarks: url-escaped to %20 Use this key in your application by passing it with the key=API_KEY parameter.
# Use '&key=AIzaSyBejvXfTfhsf20KtpGGI-S4-MpLFL72Rzg'

# https://maps.googleapis.com/maps/api/geocode/json?&address=Rue%20de%20l%27Artichaut&key=AIzaSyBejvXfTfhsf20KtpGGI-S4-MpLFL72Rzg

# !!! You have to have an API_KEY and link that key to a project where Billing is enabled.
# !!! Make sure to chose 'Google Map Platform' Billing.

import json
import urllib.parse
import urllib.request
from json import JSONDecodeError

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = 'AIzaSyBejvXfTfhsf20KtpGGI-S4-MpLFL72Rzg'

while True:
    address = input('Enter Location: ')  # rue de l'Artichaut
    if len(address) < 1:
        break

    url = service_url + urllib.parse.urlencode({'address': address})
    print(url)
    # https://maps.googleapis.com/maps/api/geocode/json?address=rue+de+l%27Artichaut
    # Spaces are encoded as '+'
    # Single quote ' (Apostrophe) is encoded as %27

    params = dict()
    params['address'] = address
    params['key'] = api_key
    url = service_url + urllib.parse.urlencode(params)
    # https://maps.googleapis.com/maps/api/geocode/json?address=Rue+de+l%27Artichaut&key=AIzaSyBejvXfTfhsf20KtpGGI-S4-MpLFL72Rzg

    print('Retrieving url:', url)
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
        continue

    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print('Lat =', lat, 'Lng =', lng)
    location = js['results'][0]["formatted_address"]
    print(location)

# Lat = 50.84838689999999 Lng = 4.374625099999999
# Artisjokstraat, 1210, Belgium
