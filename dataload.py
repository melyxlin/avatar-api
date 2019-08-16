import json
def load_characters():
    with open('./data/charactersdata.json', 'r') as f:
        return json.load(f)