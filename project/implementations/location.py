from project.data import *
from flask import jsonify

def get_all_locations():
    locations_data = load_locations()
    return jsonify(locations_data)

def get_nation(nation):
    locations_data = load_locations()
    locations = []
    for location in load_locations():
        if location['nation'] == nation:
            locations.append(location)
    return jsonify(locations)