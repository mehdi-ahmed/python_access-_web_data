import json
import ssl
import urllib.request

import twurl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

while True:
    print('')
    acct = input('Enter a Twitter account: ')
    if len(acct) < 1:
        break

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving URL', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    # print(data[:250])

    # Print headers
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('     *** No status found...')
            continue

        s = u['status']['text']
        print(' ', s[:50])
