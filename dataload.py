import json
from collections import OrderedDict

def load_characters():
    with open('./data/charactersdata.json', 'r') as f:
        return json.load(f, object_pairs_hook=OrderedDict)