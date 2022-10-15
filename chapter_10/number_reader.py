import json

filename = 'py/pcc_2e/chapter_10/numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)
