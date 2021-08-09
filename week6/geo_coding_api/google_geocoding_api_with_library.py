import json
from datetime import datetime

import googlemaps  # Needs to be installed

api_key = 'AIzaSyBejvXfTfhsf20KtpGGI-S4-MpLFL72Rzg'
gmaps = googlemaps.Client(key=api_key)

# Geocoding an address
geocode_result = gmaps.geocode("Rue de l'Artichaut")

print(json.dumps(geocode_result, indent=4))

for item in geocode_result:
    print(item["formatted_address"])  # Artisjokstraat, 1210, Belgium
    print(item["geometry"]["location"]["lat"])  # 50.84838689999999
    print(item["geometry"]["location"]["lng"])  # 4.374625099999999

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(json.dumps(reverse_geocode_result, indent=4))

for item in reverse_geocode_result:
    print(item["formatted_address"])  # Artisjokstraat, 1210, Belgium
    print(item["geometry"]["location"]["lat"])  # 50.84838689999999
    print(item["geometry"]["location"]["lng"])  # 4.374625099999999

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
