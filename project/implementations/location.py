from project.data import *
from flask import jsonify

def get_all_locations():
    locations_data = load_locations()
    return jsonify(locations_data)

def get_nation(nation):
    locations_data = load_locations()
    locations = []
    for location in locations_data:
        if location['nation'] == nation:
            locations.append(location)
    if len(locations) == 0:
            return None
    return jsonify(locations)

def get_specific_location(name):
        location_data = load_locations()
        for location in location_data:
                if location["name"] == name:
                        return jsonify(location)
        return None