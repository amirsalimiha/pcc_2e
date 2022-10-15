import json

filename = 'py/pcc_2e/chapter_10/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
