# Imprting the json module and loading the data from the file
import json
with open('snakes.json','r') as json_file:
    json_data = json.load(json_file)

print(type(json_data))


# Exploring the data
for key,value in json_data.items():
    print(f'{key} : {value}')


# Alternatively
print("*********Using keys() method***********\n")
for key in json_data.keys():
    print(f'{key} : {json_data[key]}')
