import json

personal_info = {'name': 'Roman', 'citi': 'Lviv'}

json_date = json.dumps(personal_info)
json_dict = json.loads(json_date)

json_dict['age'] = 37
json_date = json.dumps(json_dict)
print(json_date)
with open('file.json') as file:
    json.dump(json_dict, file)
# with open('file.json', 'w') as file:
#     json.dump(personal_info, file)

