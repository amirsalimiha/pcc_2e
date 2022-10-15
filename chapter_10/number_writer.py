import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'py/pcc_2e/chapter_10/numbers2.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
