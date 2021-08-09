import re

num_list = list()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue

    num = float(stuff[0])
    num_list.append(num)

print('Maximum:', max(num_list))
