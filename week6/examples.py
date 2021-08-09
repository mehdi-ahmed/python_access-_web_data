# JavaScript Object Notation (JSON) - Week 6
# Similar to Python dictionaries

import json

data = ''' {
                "name": "Chuck",
                "phone": {
                    "type": "intl",
                    "number": "+1 124 456 789"
                },
                "email": {
                    "hide": "yes"
                }
            }'''

info = json.loads(data)
print('Name:', info["name"])
print('Email Hide:', info["email"]["hide"])

# Name: Chuck
# Email Hide: yes

print('-------------------------')
data_list = ''' [ 
                    {
                        "id": "001",
                        "x": "2",
                        "name": "Chuck"
                    },
                    {
                        "id": "009",
                        "x": "27",
                        "name": "Mehdi"
                    }
            ]'''

info = json.loads(data_list)
print('User count:', len(info))

for item in info:
    print('Name:', item["name"])
    print('Id:', item["id"])
    print('Attribute:', item["x"])

# User count: 2
# Name: Chuck
# Id: 001
# Attribute: 2
# Name: Mehdi
# Id: 009
# Attribute: 27
