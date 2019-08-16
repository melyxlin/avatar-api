from dataload import *
from flask import jsonify

class charactersFilter:
    def __init__(self):
        self.__bending = ['Waterbending', 'Earthbending', 'Firebending', 'Airbending', 'Metalbending', 'Bloodbending']
        self.__gender = ['male', 'female']
        self.__ethnicity = ['Water', 'Fire', 'Air', 'Earth']
    
    def get_bendings(self):
        return self.__bending
    
    def get_genders(self):
        return self.__gender

    def get_ethnicity(self):
        return self.__ethnicity


def all_characters():
    characters_data = load_characters()
    return jsonify(characters_data)

def character(name):
    character_data  = load_characters()
    characters  = []
    for character in character_data:
        if character["name"] == name:
            characters.append(character)
    return jsonify(characters)

def benders(element):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if element in character['bending']:
            characters.append(character)
    return jsonify(characters)
    
def gender(gender):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if character['gender'] == gender:
           characters.append(character)
    return jsonify(characters)

def ethnicity(ethnicity):
    characters_data = load_characters()
    characters = []
    for character in characters_data:
        if character['ethnicity'] == ethnicity:
            characters.append(character)
    return jsonify(characters)
        

    
