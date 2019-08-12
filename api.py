from flask import Flask, request, jsonify
import json
from dataload import *

app = Flask(__name__)
app.config["DEBUG"] = True

#endpoint for mainpage
@app.route("/", methods=['GET'])
def mainPage():
    return "Avatar the Last Airbender API"

@app.route("/characters", methods=['GET'])
def get_characters():
    characters_data = load_characters()
    print(characters_data)
    return jsonify(characters_data)

@app.route("/characters/<string:name>", methods=['GET'])
def get_character(name):
    characters_data = load_characters()
    character = {}
    for char in characters_data:
        if char['name'] == name:
            character.update(char)
    return jsonify(character)

@app.route("/benders/<string:element>", methods=['GET'])
def get_benders(element):
    characters_data = load_characters()
    benders = {}
    for character in characters_data:
        if element in character['Bending']:
            benders.update(character)
    return jsonify(benders)
