import json

with open('stickers.json', 'r') as file:
    data = json.load(file)
print(data)
