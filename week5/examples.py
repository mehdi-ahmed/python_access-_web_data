# Week 5 - Data on the Web

# XML Schema = Contract

# XSD, a recommendation of the World Wide Web Consortium (W3C), specifies how to formally describe the elements in an
# Extensible Markup Language document. It can be used by programmers to verify each piece of item content in a
# document, to assure it adheres to the description of the element it is placed in.

# Parsing XML with Python

import xml.etree.ElementTree as ET

data = '''<person>
            <name>Chuck</name>
            <phone type="intl"> +1 734 303 4456</phone>
            <email hide="yes"/>
         </person>'''

data2 = '''<stuff>
                <users>
                        <user x="2">
                            <id>001</id>
                            <name>Chuck</name>
                        </user>
                        <user x="7">
                            <id>009</id>
                            <name>Mehdi</name>
                        </user>
                </users>
        </stuff>'''

# data
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)  # Name: Chuck
print('Attr:', tree.find('email').get('hide'))  # Attr: yes

print('----------------')

# data2
stuff = ET.fromstring(data2)
users = stuff.findall('users/user')
print('User count:', len(users))    # User count: 2
for user in users:
    print('Name:', user.find('name').text)
    print('Id:', user.find('id').text)
    print('Attribute:', user.get('x'))
