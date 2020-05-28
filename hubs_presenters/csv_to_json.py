import csv
import json

csv_file_path = 'permissions.csv'
json_file_path = 'permissions.json'

data = {}

with open(csv_file_path) as csv_file:
    with open(json_file_path, 'w') as json_file:
        csv_reader = csv.DictReader(csv_file)
        json_file.write('[')
        for row in csv_reader:
            json.dump(row, json_file)
            json_file.write(',\n')
        json_file.write(']')