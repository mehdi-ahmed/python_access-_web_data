# urllib is a library that does all the socket work and makes web pages look like a file

import urllib.request

f_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()

for line in f_hand:
    print(line.decode().strip())

    # But soft what light through yonder window breaks
    # It is the east and Juliet is the sun
    # Arise fair sun and kill the envious moon
    # Who is already sick and pale with grief

    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3,
# 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill':
