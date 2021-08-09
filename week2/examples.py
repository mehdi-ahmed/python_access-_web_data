# https://docs.python.org/3/library/re.html
# Example with search()
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

    # Alternative to startswith()
    if re.search('^Received:', line):
        print(line)

    # Starts with X
    if re.search('^X.*', line):
        print(line)  # X-Authentication-Warning:

    # Match any non white space one or more times
    # \S should be replaced by [:space:]

    if re.search('^X-\\S+:', line):
        print(line)  # X-Authentication-Warning:

    # X-DSPAM - Probability: 0.0000               OK
    # X- Plane is behind schedule: 2 weeks        NOK

print('-------------------')
# Examples of Reg Expressions
# [0-9]+ : One or more digits

x = 'My 2 favourite numbers are 17 and 666'
reg = re.findall('[0-9]+', x)
print(reg)  # ['2', '17', '666']
print('-------------------')

# Search for one or more Upper case vowels
vowels = re.findall('[AEIOU]+', x)
print(vowels)  # []

# Greedy Matching
# First character in the match is an F
# Last character is :
x = 'From: Using the : '
y = re.findall('^F.+:', x)
print(y)  # ['From: Using the :']

# Not greedy: Add 'y' to the expression
y = re.findall('^F.+?:', x)
print(y)  # ['From:'] It returns the shortest because it is not greedy

# Emails
print('-------------------')
x = 'From mehdi.ahmed.2009@gmail.com sat Jan 5 09:14:16 2009'
# At least one non white character ==> \S+
y = re.findall('^From (\\S+@\\S+)', x)
print(y)  # ['mehdi.ahmed.2009@gmail.com']

# Host of the email
print('-------------------')

# * = Match many Many of them
# ^ = Not
# [^ ] = Matching non blank characters
# ==>   '@([^ ]*)'
# ^From = Filter lines
y = re.findall('^From .*@([^ ]*)', x)
print(y)  # ['gmail.com']

# Escape characters
print('-------------------')
x = 'We just received $20.00 for cookies'
y = re.findall('\\$[0-9]+', x)
print(y)  # ['$20']

# More Examples
print('-------------------')
x = 'From: Using the : character'
y1 = re.findall('^F.+:', x)
y2 = re.findall('^F.+?:', x)  # non greedy
print(y1)    # ['From: Using the :']
print(y2)    # ['From:']
