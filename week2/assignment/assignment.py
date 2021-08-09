# look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
# converting the extracted strings to integers and summing up the integers.
import re
handler = open('real_data.txt')
numbers = list()
for line in handler:
    digits_in_text = re.findall('[0-9]+', line)
    for digit in digits_in_text:
        numbers.append(int(digit))

print(sum(numbers))  # 345599


