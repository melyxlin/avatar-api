from project.data import *
from flask import jsonify

def get_all_characters():
    characters_data = load_characters()
    return jsonify(characters_data)

def get_specific_character(name):
    character_data  = load_characters()
    for character in character_data:
        if character["name"] == name:
            return jsonify(character)
    return None

def get_benders(bending):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if bending in character['bending']:
            characters.append(character)
    return jsonify(characters)
    
def get_gender(gender):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if character['gender'] == gender:
           characters.append(character)
    return jsonify(characters)

def get_ethnicity(ethnicity):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if character['ethnicity'] == ethnicity:
            characters.append(character)
    return jsonify(characters)

def get_nationality(nationality):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if character['nationality'] == nationality:
            characters.append(character)
    return jsonify(characters)

def get_affiliation(affiliation):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if affiliation in character['affiliation']:
            characters.append(character)
    return jsonify(characters)
        

    
