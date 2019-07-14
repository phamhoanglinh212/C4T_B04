import json
with open('dataGet.json') as json_file:  
    data = json.load(json_file)
print(data[1]['name'])

