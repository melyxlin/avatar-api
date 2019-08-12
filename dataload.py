import json

def load_characters():
    with open('./data/characters.json', 'r') as f:
        return json.load(f)