import ssl
import urllib.request

from twurl import augment

# https://developer.twitter.com/en/apply-for-access
# Create a developer account, get it approved and save the keys in hidden.py

print("*** Calling Twitter ...")
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count': '5'})

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

headers = dict(connection.getheaders())
print(headers)
