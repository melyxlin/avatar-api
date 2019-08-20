from project.data import *
from flask import jsonify

def get_all_bendings():
    bending_data = load_bending()
    return jsonify(bending_data)

def get_specific_bending(name):
    bending_data = load_bending()
    for bending in bending_data:
        if bending["name"] == name:
            return jsonify(bending)
    return None
