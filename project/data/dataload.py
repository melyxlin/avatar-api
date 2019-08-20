import json
import os
from collections import OrderedDict

def load_characters():
        fname = os.path.join(os.path.dirname(__file__), 'charactersdata.json')
        with open(fname, 'r') as f:
                return json.load(f, object_pairs_hook=OrderedDict)

def load_locations():
        fname = os.path.join(os.path.dirname(__file__), 'locationsdata.json')
        with open (fname, 'r') as f:
                return json.load(f, object_pairs_hook=OrderedDict)

def load_bending():
        fname = os.path.join(os.path.dirname(__file__), 'bendingdata.json')
        with open (fname, 'r') as f:
                return json.load(f, object_pairs_hook=OrderedDict)